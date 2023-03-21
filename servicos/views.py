from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Categoria, Endereco, Servico, Imagem, Comment, Help
from .forms import CommentForm, ServicoForm, EndForm, ImageForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


def home(request):
    categorias = Categoria.objects.all()
    qtd_servico = Servico.objects.count()
    qtd_user = User.objects.count()

    nome = request.GET.get('nome')
    estado = request.GET.get('estado')
    cidade = request.GET.get('cidade')
    category = request.GET.get('category')

    existe = True

    servicos_list = Servico.objects.filter(status='ativo').order_by('-created_at')

    if(servicos_list.exists()): 
    
        # filter
        if nome and estado and cidade and category:
            servicos_list = Servico.objects.select_related('endereco').filter(nome__icontains=nome, endereco__estado=estado, endereco__cidade=cidade, categoria=category, status='ativo')
            
            cat = Categoria.objects.filter(id=category).first()
           

        elif estado and cidade and category:
            servicos_list = Servico.objects.select_related('endereco').filter(endereco__estado=estado, endereco__cidade=cidade, categoria=category, status='ativo')

            cat = Categoria.objects.filter(id=category).first()
           

        elif estado and cidade:
            servicos_list = Servico.objects.select_related('endereco').filter(endereco__estado=estado, endereco__cidade=cidade, status='ativo')
           
        elif nome:
            
            servicos_list = Servico.objects.filter(nome__icontains=nome, status='ativo')
        elif category:
            servicos_list = Servico.objects.select_related('endereco').filter(categoria=category, status='ativo')
            
            cat = Categoria.objects.filter(id=category).first()
    else:
        existe = False

    paginator = Paginator(servicos_list, 6)

    page = request.GET.get('page')
    servicos = paginator.get_page(page)

    context = { 
        'servicos': servicos,
        'categorias': categorias,
        'qtd_user': qtd_user,
        'qtd_servico': qtd_servico,
        'existe': existe
    }
    
    return render(request, 'index.html', context)



def about(request):
    qtd_servicos = Servico.objects.count()
    qtd_user = User.objects.count()

    context = {
        'qtd_servicos': qtd_servicos,
        'qtd_user': qtd_user,
    }

    return render(request, 'servico/about.html', context)

@login_required
def addServico(request):

    if request.method == 'POST': 
        servicoForm = ServicoForm(request.POST)
        endForm = EndForm(request.POST)
        imageForm = ImageForm(request.POST, request.FILES)
        images = request.FILES.getlist('image')

        if servicoForm.is_valid() and endForm.is_valid():
            servico = servicoForm.save(commit=False)
            endereco = endForm.save(commit=False)
            endereco.save()

            servico.user = request.user
            
            servico.endereco_id = endereco.id
            
            if images != []:
                servico.capa = images.pop(0)
            
            servico.save()

            # upload das images
            for image in images:
                image_instance = Imagem(image=image, servico=servico)
                image_instance.save()
            
            messages.success(request, 'Serviço adicionado com sucesso..')
            return redirect('dashboard')
       
    else:
        servicoForm = ServicoForm()
        endForm = EndForm()
        imageForm = ImageForm()


        context = {
            'servicoForm': servicoForm,
            'endForm': endForm,
            'imageForm': imageForm
        
        }

        return render(request, 'servico/addservico.html', context)

def servicoView(request, id):
    # Objects 
    servico = get_object_or_404(Servico, pk=id)
    comments = Comment.objects.filter(servico_id=id)
    qtd_comments = len(comments)
    images = Imagem.objects.filter(servico_id=id)

    user = User.objects.filter(id=servico.user_id)
    dono = ''
    for x in user:
        dono = x.first_name+" "+x.last_name

    # Commet form 
    if request.method == 'POST': 
        commentForm = CommentForm(request.POST)

        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.servico_id = id
            comment.save()
        
            messages.success(request, 'Comentario adicionado com sucesso..')
            
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    else:
        commentForm = CommentForm()

        context = {
            'servico': servico, 
            'comments': comments, 
            'qtd_comments': qtd_comments, 
            'images': images,
            'commentForm': commentForm,
            'servico':servico,
            'dono': dono
        }

        return render(request, 'servico/servicoView.html', context)

@login_required
def dashboard(request):
    
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    achou = False # caso encontre algo na busca
    exite = True # caso exita algum serviço 
    status = False # active or not 
    
    servicos_list = Servico.objects.all().order_by('-created_at').filter(user=request.user)

    if(servicos_list.exists()): 
        if search:
            servicos_list = Servico.objects.filter(nome__icontains=search, user=request.user)

            if(servicos_list.exists()):
                achou = True
        elif filter and filter != "todos":
            servicos_list = Servico.objects.filter(status=filter, user=request.user)

            if(servicos_list.exists()):
                status = True

    else:
        exite = False

    paginator = Paginator(servicos_list, 8)

    page = request.GET.get('page')
    servicos = paginator.get_page(page)

    context = {
        'servicos': servicos,
        'achou': achou,
        'exite': exite,
        'status': status
        
    }

    return render(request, 'servico/dashboard.html', context)

@login_required
def removeServico(request, id):
    servico = get_object_or_404(Servico, pk=id)
    servico.delete()

    messages.success(request, 'Serviço removido com sucesso..')
    
    return redirect('dashboard')

@login_required
def editServico(request, id):
    servico = get_object_or_404(Servico, pk=id)
    endereco = Endereco.objects.filter(id=servico.endereco_id).first()
    
    servicoForm = ServicoForm(instance=servico)
    endForm = EndForm(instance=endereco)

    if(request.method == 'POST'):
        servicoForm = ServicoForm(request.POST, instance=servico)
        endForm = EndForm(request.POST, instance=endereco)

        if servicoForm.is_valid() and endForm.is_valid():
            servico.save()
            endereco.save()

            messages.success(request, 'Serviço alterado com sucesso..')
            return redirect('dashboard')
    
    else:
        context = {
            'servicoForm': servicoForm,
            'endForm': endForm,
        }
        
        return render(request, 'servico/editservico.html', context)

def help(request):
    search = request.GET.get('search_help')
    list_help = Help.objects.all()
    achou = True
    
    if search:
        list_help = Help.objects.filter(titulo__icontains=search)

        if(not(list_help.exists())):
            achou = False
   
    paginator = Paginator(list_help, 8)
    page = request.GET.get('page')
    helps = paginator.get_page(page)
    
    return render(request,'servico/help.html', {'helps': helps, 'achou': achou})



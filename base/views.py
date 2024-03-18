import json
import ast
from django.conf import settings
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest, FileResponse, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import SOW, Save_Lesson
from .Pdf_Generator.main import generatepdf

# Create your views here.
@csrf_exempt
def insert_sow(request):
  if request.method == 'POST':
    received_data = json.loads(request.body.decode('utf-8'))
    get_data = received_data.get('input', '')
    
    sow_id = f'{get_data[0]}{get_data[1]}'
    
    try:
      SOW.objects.get(sow_id=sow_id)
      
      if get_data[3] != '':  
        send_data = {
          'input': f"SOW '{sow_id}' already exists."
        }
      else:
        send_data = {
          'input': "Please fill in the fields."
        }
    except SOW.DoesNotExist:
      SOW.objects.create(
        sow_id = sow_id,
        contents = get_data
      )
      
      send_data = {
        'input': 'Progress has been saved.',
        'input2': get_data,
      }
    
    return JsonResponse(send_data)
  else:
    return HttpResponseBadRequest("Invalid request method. Please use POST.")


@csrf_exempt
def fetch_sow(request):
  if request.method == 'POST':
    received_data = json.loads(request.body.decode('utf-8'))
    get_data = received_data.get('input', '')
    sow_id = int(get_data)
    
    retrieved_data_from_SOW = SOW.objects.get(sow_id=sow_id)
    fetch_data = retrieved_data_from_SOW.contents
    input = []
    
    for i in range(len(fetch_data)):
      if i == 7 or i == 8 or i == 9 or i == 10:
        input.append(ast.literal_eval(fetch_data[i]))
      else:
        input.append(fetch_data[i])
    
    send_data = {
      'input': input,
    }
    
    return JsonResponse(send_data)
  

@csrf_exempt
def save_new_sow(request):
  if request.method == 'POST':
    received_data = json.loads(request.body.decode('utf-8'))
    get_data = received_data.get('input', '')
    sow_id = f'{get_data[0]}{get_data[1]}'
    
    fetch_data = SOW.objects.get(sow_id=int(sow_id))
    fetch_data.contents = get_data
    fetch_data.save()
    
    input = 'Progress have been saved'
    
    send_data = {
      'input': input,
    }
    
    return JsonResponse(send_data) 
  
  
@csrf_exempt
def generate_pdf(request):
  if request.method == 'POST':
    received_data = json.loads(request.body.decode('utf-8'))
    get_data = received_data.get('input', '')
    
    return(generatepdf(get_data))
  
  
@csrf_exempt
def save_lesson(request):
  if request.method == 'POST':
    received_data = json.loads(request.body.decode('utf-8'))
    get_data = received_data.get('input' ,'')
    check = received_data.get('check', '')
    user = Save_Lesson.objects.get(name_id=request.user.id)
    
    if check:
      year = get_data[0][1]
      current_lesson = get_data[0][4]
      all_saved_lessons = []
      all_check_lessons = []
      
      for lesson in user.contents:
        unstring_list = ast.literal_eval(lesson)
        all_saved_lessons.append(unstring_list)
      
      if all_saved_lessons != []:
        for _, check_year_lesson in enumerate(all_saved_lessons):
          get_year = check_year_lesson[0][0][1]
          get_lesson = check_year_lesson[0][0][4]
          all_check_lessons.append([get_year, get_lesson])
          
        for i in all_check_lessons:
          if i[0] == year and i[1] == current_lesson:
            check = True
          else:
            check = False
        
        if check:
          send_data = {
            'input': 'Duplication of lesson detected',
            'check': check,
          }
        else:
          user.contents.append([get_data])
          user.save()
     
          send_data = {
            'input': 'Lesson Saved',
            'check': check,
          }
          
        return JsonResponse(send_data)
      else:
      
        user.contents.append([get_data])
        user.save()

        check = False
        
        send_data = {
          'input': 'Lesson Saved',
          'check': check,
        }
        return JsonResponse(send_data)
    else:
      user.contents.append([get_data])
      user.save()

      check = False
      
      send_data = {
        'input': 'Lesson saved!',
        'check': check,
      }
      return JsonResponse(send_data)
  
  
@csrf_exempt
def load_lesson(request):
  if request.method == 'GET':
    user_lessons = Save_Lesson.objects.get(name_id=request.user.id)
    lesson_info = []
    new_list = [] 
    
    for i, lesson in enumerate(user_lessons.contents):
      new_list.append(ast.literal_eval(lesson))
      
    for i, lesson in enumerate(new_list):
      lesson_info.append([lesson[0][0][1], lesson[0][0][4], lesson[0][0][5]])
      
    send_data = {
      'input': lesson_info,
    }
    
    return JsonResponse(send_data)
  
  
@csrf_exempt
def insert_load_lesson(request):
  if request.method == 'POST':
    received_data = json.loads(request.body.decode('utf-8'))
    get_data = received_data.get('input', '')
    
    load_lesson = Save_Lesson.objects.get(name_id=request.user.id)
    get_load_lesson = load_lesson.contents[get_data]
    load_lesson.contents.remove(get_load_lesson)
    load_lesson.contents.insert(0, get_load_lesson)
    load_lesson.save()
    
    send_data = {
      'input': ast.literal_eval(get_load_lesson),
    }
    
    return JsonResponse(send_data)
  
  
@csrf_exempt
def delete_lesson(request):
  if request.method == 'POST':
    received_data = json.loads(request.body.decode('utf-8'))
    get_data = int(received_data.get('input', ''))
    print(get_data)
    
    saved_lesson = Save_Lesson.objects.get(name_id=request.user.id)
    get_lesson = saved_lesson.contents
    unstring_lessons = []
    
    for i in get_lesson:
      lesson = ast.literal_eval(i)
      unstring_lessons.append(lesson)
      
    for i, j in enumerate(unstring_lessons):
      if i == get_data:
        unstring_lessons.remove(j)
    
    saved_lesson.contents = unstring_lessons
    saved_lesson.save()
    send_data = {
      'input': 'Lesson have been deleted',
    }
    return JsonResponse(send_data)
  
  
@csrf_exempt
def login_page(request):
  if request.method == 'POST':
    received_data = json.loads(request.body.decode('utf-8'))
    get_data = received_data.get('input', '')
    
    user = authenticate(request, username=get_data[0], password=get_data[1])
    
    if user != None:
      login(request, user)

      send_data = {
        'input': 'Login Successful',
        'check': True,
      }
      
      return JsonResponse(send_data)
    else:
      send_data = {
        'input': "User does not exist. Please check your username and password for any errors. If you haven't register, please click the 'register' below",
        'check': False,
      }
      
      return JsonResponse(send_data)
    
    
@csrf_exempt
def register_page(request):
  if request.method == 'POST':
    received_data = json.loads(request.body.decode('utf-8'))
    
    form = UserCreationForm(data=received_data)
    
    if form.is_valid(): 
      try:
        user = form.save()
        login(request, user)
        
        Save_Lesson.objects.create(
          name_id = user
        )
        
        send_data = {
          'input': 'Registration Successful',
          'check': True,
        }
        return JsonResponse(send_data)
      except:
        send_data = {
        'input': 'User already exists. Try new username',
        'check': False,
      }
      return JsonResponse(send_data)
    else:
      send_data = {
        'input': 'Form is not valid.',
        'check': False,
      }
      return JsonResponse(send_data)

@csrf_exempt
def first_login(request):
  if request.method == 'GET':
    send_data = {
      'input': [request.user.username, request.user.is_authenticated],
    }
    return JsonResponse(send_data)


@login_required
@csrf_exempt
def logout_page(request):
  if request.method == 'GET':
    logout(request)
    
    send_data = {
      'input': 'Logout Successful',
    }
    return JsonResponse(send_data)


class RenderPdfDSKP():
  @csrf_exempt
  def view_pdf_DSKPYEAR1(request):
    type = 'DSKP'
    year = 'YEAR1'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)
  
  def view_pdf_DSKPYEAR2(request):
    type = 'DSKP'
    year = 'YEAR2'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)
  
  def view_pdf_DSKPYEAR3(request):
    type = 'DSKP'
    year = 'YEAR3'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)
  
  def view_pdf_DSKPYEAR4(request):
    type = 'DSKP'
    year = 'YEAR4'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)
  
  def view_pdf_DSKPYEAR5(request):
    type = 'DSKP'
    year = 'YEAR5'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)

  def view_pdf_DSKPYEAR6(request):
    type = 'DSKP'
    year = 'YEAR6'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)


class RenderPdfSOW():
  @csrf_exempt
  def view_pdf_SOWYEAR1(request):
    type = 'SOW'
    year = 'YEAR1'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)
  
  def view_pdf_SOWYEAR2(request):
    type = 'SOW'
    year = 'YEAR2'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)
  
  def view_pdf_SOWYEAR3(request):
    type = 'SOW'
    year = 'YEAR3'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)
  
  def view_pdf_SOWYEAR4(request):
    type = 'SOW'
    year = 'YEAR4'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)
  
  def view_pdf_SOWYEAR5(request):
    type = 'SOW'
    year = 'YEAR5'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)

  def view_pdf_SOWYEAR6(request):
      type = 'SOW'
      year = 'YEAR6'
          
      context = {
        'input': f'documents/{type}{year}.pdf',
      }
          
      return render(request, f'base/document.html' ,context)


class RenderPdfTEXTBOOK():
  @csrf_exempt
  def view_pdf_TEXTBOOKYEAR1(request):
    type = 'TEXTBOOK'
    year = 'YEAR1'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)
  
  def view_pdf_TEXTBOOKYEAR2(request):
    type = 'TEXTBOOK'
    year = 'YEAR2'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)
  
  def view_pdf_TEXTBOOKYEAR3(request):
    type = 'TEXTBOOK'
    year = 'YEAR3'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)
  
  def view_pdf_TEXTBOOKYEAR4(request):
    type = 'TEXTBOOK'
    year = 'YEAR4'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)
  
  def view_pdf_TEXTBOOKYEAR5(request):
    type = 'TEXTBOOK'
    year = 'YEAR5'
        
    context = {
      'input': f'documents/{type}{year}.pdf',
    }
        
    return render(request, f'base/document.html' ,context)

  def view_pdf_TEXTBOOKYEAR6(request):
      type = 'TEXTBOOK'
      year = 'YEAR6'
          
      context = {
        'input': f'documents/{type}{year}.pdf',
      }
          
      return render(request, f'base/document.html' ,context)


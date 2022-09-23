from django.shortcuts import render

from editor.models import Editor



def Demo(request):
    print('....................')
    if request.method == 'POST':
        Editor.objects.create(
            Description = request.POST['Description']
        )
    return render(request,"home.html")

    



# if request.method=='POST':
        
#         description = request.POST['content']
#         print('--------------',description)
#         text = Editor.objects.create(Description=description)
#         text.save()
#     return render(request,"home.html")
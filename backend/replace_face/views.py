from django.http import JsonResponse, HttpResponse
from .models import FaceReplace 
import subprocess
import datetime
from backend.settings import BASE_DIR, ROOP_DIR
import os
import base64

# Create your views here.
def replace_face(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        print(image)
        video = request.FILES.get('video')
        print(video)
        
        if not image or not video:
            return HttpResponse('Forbidden')
        # Save the uploaded files
        face_replace = FaceReplace.objects.create(image=image, video=video)

        # Execute the script to replace face
        source_path = face_replace.image.path
        target_path = face_replace.video.path

        print("source path:", source_path)
        print("target path:", target_path)

        video_name = str(datetime.datetime.now()).replace(':', '-').replace(' ', '-').replace('.', '-') + '.mp4'
        output_path = str(BASE_DIR) + '\\' +  'output\\videos\\' + video_name
        print(output_path)

        venv_path = str(ROOP_DIR).replace('\\', '/') + "/roop/venv"
        print(venv_path)

        # Build the activation command based on the platform
        activate_cmd = f"cmd /K \"cd /d {str(ROOP_DIR).replace('\\', '/')}/roop && {venv_path}/Scripts/activate.bat && python run.py -s {source_path} -t {target_path} -o {output_path}\""
        print(activate_cmd)
        # Execute the activation command in a new shell session
        process = subprocess.run(activate_cmd, shell=True)
        # process = subprocess.run(['start', 'cmd', '/c', activate_cmd], shell=True)

        video_path = str(BASE_DIR) + "\\output\\videos\\" + video_name
       
        with open(video_path, 'rb') as f:
            video_data = f.read()

         # Convert binary data to base64-encoded string
        video_base64 = base64.b64encode(video_data).decode('utf-8')

        return JsonResponse({'message': 'Face replaced successfully', "video_path": video_base64})

        # return JsonResponse({'message': 'Face replaced successfully', "video_path": video_name})
        # if process.returncode == 0:
        #     return JsonResponse({'message': 'Face replaced successfully', "video_path": output_path})
        # else:
        #     return JsonResponse({'error': 'Error occurred while processing'}, status=500)
    
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
def get_video(request, video_name):
    video_path = str(BASE_DIR) + "\\output\\videos\\" + video_name
    with open(video_path, 'rb') as f:
        video_data = f.read()
    
    response = HttpResponse(video_data, content_type='video/mp4')
    response['Content-Length'] = os.path.getsize(video_path)
    return response

# def get_video(request):
#     print('complete')
#     print(request.POST)
#     if request.method == 'POST':
#         video_path = str(BASE_DIR) + "\\output\\videos\\" + request.POST.get('video_name')
#         print(video_path)
        
#         with open(video_path, 'rb') as f:
#             video_data = f.read()
        
#         response = HttpResponse(video_data, content_type='video/mp4')
#         response['Content-Length'] = os.path.getsize(video_path)
#         return response
    
def display(request):
    print('ok')
    return HttpResponse('redirect')
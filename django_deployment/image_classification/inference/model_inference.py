import torch 
import torchvision
import os
from torchvision import transforms
from PIL import Image
import json
from pathlib import Path
from django.conf import settings


def classify(media_root, file_name):
    image_path = Path(media_root + '/' + file_name)
    image = Image.open(image_path)
    transform = transforms.Compose([transforms.Resize((224, 224)),                                   
                                    transforms.ToTensor(),                     
                                    transforms.Normalize(                      
                                    mean=[0.485, 0.456, 0.406],                
                                    std=[0.229, 0.224, 0.225])])
    image = transform(image)
    image = torch.unsqueeze(image, 0)
    torch_home = os.path.join(settings.BASE_DIR, 'image_classification/static/models')
    os.environ['TORCH_HOME'] = torch_home
    resnet = torchvision.models.resnet18(pretrained=True)
    resnet.eval()
    output = resnet(image)
    value, index = torch.max(output, 1)
     
    # percentage = torch.nn.functional.softmax(output, dim=1)[0] * 100
    # print(percentage[index[0]].item())
    # #print(labels[index[0]], percentage[index[0]].item())
    # print(value)

    #reading labels
    class_idx = json.load(open(os.path.join(torch_home, 'imagenet_class_index.json')))
    idx2label = [class_idx[str(k)][1] for k in range(len(class_idx))]
    return idx2label[index.item()]
    #print(idx2label[index.item()])

# image = Image.open('../static/uploaded_media/dogs.jpg')
# classify(image)
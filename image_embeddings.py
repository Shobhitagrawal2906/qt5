import torch
import torchvision.models as models
from torchvision import transforms
from PIL import Image
from database import Qdrant

class ImageEmbeddings:
    def __init__(self) -> None:
        self.resnet152_torch = models.resnet152(weights='ResNet152_Weights.DEFAULT')
        self.resnet152 = torch.nn.Sequential(*(list(self.resnet152_torch.children())[:-1]))
        self.resnet152_torch.eval()
        self.preprocess = transforms.Compose([
                                transforms.Resize((224,224)),
                                transforms.ToTensor(),
                                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                            ])
        
        self.database_object = Qdrant('http://localhost:6333')
        
    def calculate_tensor(self,image_path):
        img = Image.open(image_path).convert("RGB")

        # Apply the preprocessing steps to the image
        img_tensor = self.preprocess(img).unsqueeze(0)
        with torch.no_grad():
            # Get the image features from the ResNet-152 model
            img_features = self.resnet152(img_tensor)

        embeddings = img_features.squeeze()
        self.database_object.insert_data(embeddings)

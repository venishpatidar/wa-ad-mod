from transformers import AutoConfig, AutoModelForSequenceClassification, AutoTokenizer
import torch

class AdsMod:
    """
        Model init method
        base model used = bloom-560m
        model_path: takes the path of saved model weights
    """
    def __init__(self,model_path:str="./") -> None:
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenize = lambda input: tokenizer(input, truncation=True, padding="max_length", max_length=256,return_tensors="pt").to(device)
        self.model.to(device)

    """
        predict 
        takes text as input and classifies the text
        returns 0 or 1
    """
    def predict(self,text:str) -> int:
        input = self.tokenize(text)
        with torch.no_grad():
            output = self.model(**input)
        predicted_class = torch.argmax(output.logits, dim=1).item()
        return predicted_class

if __name__=="__main__":
    model = AdsMod('venishpatidar/wa-ad-mod')
    text = "Hi I am text classifier, will help you in deleteing housing ads message"
    print("Ad" if model.predict(text) else "Safe")
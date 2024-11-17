from transformers import AutoTokenizer, AutoModelForCausalLM
import threading

tokenizer = None
model = None
model_loaded = False  # Flag, um den Ladezustand des Modells zu verfolgen

def initialize_model(script_dir, local_model_path, suggestion_label, root):
    global tokenizer, model, model_loaded
    try:
        tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono", cache_dir=script_dir)
        tokenizer.pad_token = tokenizer.eos_token
        model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono", cache_dir=script_dir, ignore_mismatched_sizes=True)

        # Manuell pad_token_id setzen
        model.config.pad_token_id = tokenizer.eos_token_id

        tokenizer.save_pretrained(local_model_path)
        model.save_pretrained(local_model_path)
        model_loaded = True
        root.after(0, lambda: suggestion_label.config(text="Modell geladen"))
    except Exception as e:
        print(f"Fehler beim Laden des Modells: {e}")
        model_loaded = False

def generate_code_suggestion(input_text, suggestion_label, root):
    if not model_loaded:
        root.after(0, lambda: suggestion_label.config(text="Modell wird geladen, bitte warten..."))
        return

    def background_task():
        try:
            input_ids = tokenizer.encode(input_text, return_tensors="pt")
            attention_mask = input_ids.ne(tokenizer.pad_token_id).float()
            output = model.generate(input_ids, attention_mask=attention_mask, max_new_tokens=30, num_return_sequences=1)
            generated_code = tokenizer.decode(output[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
        except Exception as e:
            generated_code = f"Fehler bei der Generierung: {str(e)}"
        root.after(0, lambda: suggestion_label.config(text=generated_code))

    threading.Thread(target=background_task).start()

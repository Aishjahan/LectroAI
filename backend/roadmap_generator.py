from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_learning_roadmap(topic: str) -> str:
    prompt = (
        f"Act like an expert tutor. Create a 4-week personalized roadmap to learn '{topic}'. "
        # f"Include weekly goals and key topics to cover. Use simple language for students."
    )

# Generate output
    result = generator(
        prompt,
        max_new_tokens=1000,
        temperature=1.0,
        do_sample=True,     
        top_p=0.95,
        top_k=50
    )[0]["generated_text"]

    return result
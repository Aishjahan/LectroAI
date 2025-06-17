from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# Step 1: Question Generation
qg_model_name = "valhalla/t5-small-qa-qg-hl"
qg_tokenizer = AutoTokenizer.from_pretrained(qg_model_name)
qg_model = AutoModelForSeq2SeqLM.from_pretrained(qg_model_name)

# Step 2: Answer Extraction
qa_pipeline = pipeline("question-answering", 
                      model="distilbert-base-cased-distilled-squad",
                      tokenizer="distilbert-base-cased-distilled-squad")

def generate_qa_pairs(text, num_questions=7):
    # Generate questions
    input_text = f"generate questions: {text}"
    inputs = qg_tokenizer(input_text, return_tensors="pt", max_length=1000, truncation=True)
    
    outputs = qg_model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=128,
        num_return_sequences=num_questions,
        do_sample=True,
        top_p=0.95,
        temperature=0.7
    )
    
    questions = [qg_tokenizer.decode(output, skip_special_tokens=True) 
                for output in outputs]
    
    # Get answers for each question
    qa_pairs = []
    for question in set(questions):  # Remove duplicates
        if question.endswith("?") and len(question) > 5:
            answer = qa_pipeline(
                question=question,
                context=text,
                max_answer_len=50
            )['answer']
            qa_pairs.append((question, answer))
    
    return qa_pairs[:num_questions]  # Return requested number of pairs

# Example usage
if __name__ == "__main__":
    sample_text = """The Future of Renewable Energy

Renewable energy sources, such as solar, wind, hydro, and geothermal, have become increasingly crucial in the global effort to combat climate change and reduce reliance on fossil fuels. The transition to renewable energy is not just a necessity but an opportunity to create a sustainable future for our planet. As technology advances and economies of scale drive down costs, renewable energy is poised to play a dominant role in the world's energy landscape. This essay explores the current state of renewable energy, technological advancements, challenges, and the potential future trajectory.

Current State of Renewable Energy

The past decade has seen remarkable growth in the adoption of renewable energy sources. Solar and wind power, in particular, have witnessed exponential growth. According to the International Renewable Energy Agency (IRENA), renewable energy accounted for nearly 72% of the total global power expansion in 2019. Solar power has become the fastest-growing energy source, with significant installations across various regions. Wind power, both onshore and offshore, has also seen substantial investment and capacity expansion.

Technological Advancements

Advancements in technology have been a driving force behind the rapid growth of renewable energy. Innovations in solar panel efficiency, wind turbine design, energy storage, and grid integration have made renewable energy more reliable and cost-effective.

Solar Power:

The efficiency of solar panels has increased dramatically over the years. The development of photovoltaic cells with higher energy conversion rates has made solar power a viable option for both residential and commercial use.

Bifacial solar panels, which can capture sunlight from both sides, have further improved energy yield. These panels are particularly effective in areas with high reflective surfaces, such as snow-covered regions or rooftops.

Solar power plants have also benefited from innovations in tracking systems. Dual-axis trackers, for example, allow solar panels to follow the sun's trajectory more accurately, maximizing energy capture throughout the day.

Wind Power:

Wind turbine technology has evolved significantly, with larger and more efficient turbines being developed. Modern turbines can capture wind at higher altitudes, where it is stronger and more consistent.

Offshore wind farms have gained traction due to their ability to harness powerful ocean winds. Floating wind turbines, anchored to the seabed, are a promising development that allows for the installation of wind farms in deeper waters.

Improvements in materials and design have also reduced the noise and visual impact of wind turbines, addressing some of the common concerns associated with wind energy.

Energy Storage:

The intermittent nature of renewable energy sources, such as solar and wind, has necessitated advancements in energy storage solutions. Battery technology, particularly lithium-ion batteries, has seen significant improvements in capacity, efficiency, and lifespan.

Grid-scale energy storage systems, such as pumped hydro storage and compressed air energy storage, have been developed to store excess energy during periods of high generation and release it during peak demand.

Emerging technologies, like flow batteries and solid-state batteries, hold the promise of even more efficient and sustainable energy storage solutions.

Challenges and Solutions

While renewable energy has made significant strides, several challenges must be addressed to achieve a fully sustainable energy future.

Grid Integration:

Integrating renewable energy into existing power grids requires substantial upgrades and modernization. The variability of solar and wind power necessitates a flexible and resilient grid that can balance supply and demand in real time.

Smart grid technologies, which use advanced sensors and automation, can help manage the complexities of renewable energy integration. These technologies enable better monitoring, control, and optimization of energy flows.

Energy Storage:

The storage of renewable energy remains a critical challenge. While battery technology has improved, there is still a need for more efficient and cost-effective storage solutions.

Investment in research and development of new storage technologies, such as hydrogen fuel cells and supercapacitors, is essential to overcoming this challenge.

Policy and Regulation:

Government policies and regulations play a vital role in promoting renewable energy adoption. Incentives, subsidies, and carbon pricing mechanisms can accelerate the transition to renewable energy.

International cooperation and agreements are also crucial in addressing global climate change and promoting renewable energy investments across borders.

Public Perception and Social Acceptance:

Public perception and social acceptance of renewable energy projects can influence their success. Addressing concerns related to land use, noise, and visual impact is essential to gaining public support.

Community involvement and education about the benefits of renewable energy can help build positive attitudes and acceptance.

The Future Trajectory

The future of renewable energy is bright, with several trends and developments shaping its trajectory.

Decentralization:

The energy landscape is shifting towards decentralization, with distributed energy resources (DERs) becoming more prevalent. Rooftop solar panels, small wind turbines, and community energy projects empower individuals and communities to generate their own renewable energy.

Electrification:

Electrification of various sectors, including transportation and heating, is a key trend. Electric vehicles (EVs) and heat pumps, powered by renewable energy, can significantly reduce greenhouse gas emissions.

Green Hydrogen:

Green hydrogen, produced through electrolysis using renewable energy, holds immense potential as a clean fuel for industries, transportation, and power generation. Investment in green hydrogen infrastructure and technology is expected to grow in the coming years.

International Cooperation:

Global cooperation and partnerships will be essential in achieving renewable energy goals. Sharing best practices, technology transfer, and financial support for developing countries can accelerate the transition to a sustainable energy future.

Conclusion

The future of renewable energy is promising, driven by technological advancements, supportive policies, and growing public awareness. While challenges remain, the potential benefits of renewable energy—reduced greenhouse gas emissions, energy security, and economic growth—make it a critical component of a sustainable future. By investing in research, innovation, and international cooperation, we can create a world where clean, renewable energy powers our lives and protects our planet for future generations."""
    
    qa_pairs = generate_qa_pairs(sample_text, num_questions=7)
    
    print("High-Quality QA Pairs:")
    for i, (q, a) in enumerate(qa_pairs, 1):
        print(f"{i}. Question: {q}")
        print(f"   Answer: {a}\n")
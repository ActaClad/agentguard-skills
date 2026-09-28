import OpenAI from "openai";

const client = new OpenAI();
const response = await client.chat.completions.create({
  model: "gpt-4o-mini",
  messages: [{ role: "user", content: "Reply with the word ready." }],
});

console.log(response.choices[0]?.message?.content ?? "No response");

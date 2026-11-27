import { ChatBedrockConverse } from "@langchain/aws";
import { tool } from "@langchain/core/tools";
import { createReactAgent } from "@langchain/langgraph/prebuilt";
import { z } from "zod";

const getOrderStatus = tool(
  async ({ orderId }) => JSON.stringify({ orderId, status: "shipped" }),
  {
    name: "get_order_status",
    description: "Look up the status of an order by its id.",
    schema: z.object({ orderId: z.string() }),
  },
);

const model = new ChatBedrockConverse({
  model: "anthropic.claude-3-haiku-20240307-v1:0",
  region: process.env.AWS_REGION ?? "us-east-1",
});

const agent = createReactAgent({ llm: model, tools: [getOrderStatus] });
const result = await agent.invoke({
  messages: [{ role: "user", content: "What is the status of order A-100?" }],
});

console.log(result.messages.at(-1)?.content ?? "No response");

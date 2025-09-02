export let assistantId = "asst_dr5AgQnhhhnef5OSMzQ9zdk9"; // set your assistant ID here

if (assistantId === "") {
  assistantId = process.env.OPENAI_ASSISTANT_ID;
}

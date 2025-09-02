```rst
.. module:: src.ai.dialogflow
```

<TABLE >
<TR>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/README.MD'>[Root ↑]</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/README.MD'>src</A> /
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/ai/README.MD'>ai</A> /
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/ai/dialogflow/about.md'>About dialogflow model</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/ai/dialogflow/readme.ru.md'>Русский</A>
</TD>
</TABLE>

https://dialogflow.com/docs/getting-started/basics

### **dialogflow**

Dialogflow integration module.  
Provides capabilities for natural language understanding (NLU) 
and creating conversational AI applications. It includes the following main features:

- **Intent Detection:** Determines user intents based on the input text.
- **Entity Recognition:** Extracts key data from user phrases.
- **Contexts:** Manages the conversation by retaining information about the current state of the dialogue.
- **Integrations:** Supports integration with various platforms such as Google Assistant, Facebook Messenger, Slack, Telegram, and others.
- **Webhook:** Supports Webhook integrations for calling external services and APIs.

Example usage of the **dialogflow** submodule:

```python
from src.ai.dialogflow import Dialogflow

project_id = "your-project-id"
session_id = "unique-session-id"

dialogflow_client = Dialogflow(project_id, session_id)

# Example usage of methods
intent_response = dialogflow_client.detect_intent("Hello")
print("Detected Intent:", intent_response)

intents = dialogflow_client.list_intents()
print("List of Intents:", intents)

new_intent = dialogflow_client.create_intent(
    display_name="NewIntent",
    training_phrases_parts=["new phrase", "another phrase"],
    message_texts=["This is a new intent"]
)
print("Created Intent:", new_intent)

# Deleting an intent (make sure to replace intent_id with a real ID)
# dialogflow_client.delete_intent("your-intent-id")
```

# Specify the sequence of objects and actions
sequence = [
    {"target_object": "Google-Icon", "action": "click"},
    {"target_object": "newpage",  "action": "click_then_type", "text": "mail.google.com"},
    {"target_object": "unread_email", "action": "click"},
    {"target_object": "newpage",  "action": "click_then_type", "text": "chat.openai.com"},
    {"target_object": "chatgptinput", "action": "click_type", "text": "Please answer this email without subject"},
    {"target_object": "gmailicon", "action": "click"}, 
    {"target_object": "reply", "action": "click_then_paste"}, 
    {"target_object": "send", "action": "click"},
    {"target_object": "back", "action": "click"}
]

loop_sequence = [
    {"target_object": "unread_email", "action": "click"},
    {"target_object": "chatgpticon", "action": "click"},
    {"target_object": "chatgptinput", "action": "click_type", "text": "Please answer this email without subject"},
    {"target_object": "gmailicon", "action": "click"},
    {"target_object": "reply", "action": "click_then_paste"},
    {"target_object": "send", "action": "click"},
    {"target_object": "back", "action": "click"}
]
import time
from main_sequence import execute_main_sequence
from email_actions import check_unread_emails

if __name__ == "__main__":
    execute_once = True
    second_block_execute = True
    
    while execute_once:
        time.sleep(2)
        has_unread_emails = execute_main_sequence()
        if not has_unread_emails:
            print('No emails to answer...')
            second_block_execute = False
            break
        execute_once = False
    
    if second_block_execute:  # This block will run only if the first block did not break.
        while True:
            time.sleep(2)
            has_unread_emails = check_unread_emails()
            if not has_unread_emails:
                print('No emails to answer...')
                break
            time.sleep(2)

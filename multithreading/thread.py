import threading
import time

# Target function for sending SMS (no return value required)
def send_sms(number, name):
    time.sleep(2)  # 2-second delay for SMS
    print(f"SMS Sent using target function. {number} and {name}")

# Target function for sending Email (no return value required)
def send_email():
    time.sleep(3)  # 3-second delay for Email
    print("Email Sent using target function.")

# Target function for calculating ETA (no return value required)
def calculate_eta():
    time.sleep(5)  # 5-second delay for ETA calculation
    print("ETA Calculated using target function. Estimated Time: 25 minutes.")

if __name__ == "__main__":
    # Create Thread objects and pass target functions to them
    sms_thread    = threading.Thread(target=send_sms, kwargs = {"number": 12345, "name": "rupesh"})
    email_thread  = threading.Thread(target=send_email)
    eta_thread    = threading.Thread(target=calculate_eta)

    print("Task Started.\n")

    # Start all threads
    sms_thread.start()
    print("Task 1 ongoing...")

    email_thread.start()
    print("Task 2 ongoing...")

    eta_thread.start()
    print("Task 3 ongoing...")

    # Wait for all threads to finish
    sms_thread.join()
    email_thread.join()
    eta_thread.join()

    print("All tasks completed.")
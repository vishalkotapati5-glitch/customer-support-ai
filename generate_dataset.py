import pandas as pd

tickets = [

    # =========================
    # ACCOUNT ISSUES
    # =========================

    ("I forgot my password and cannot access my account.", "Account Issue", "Low"),
    ("I forgot my username and cannot sign in.", "Account Issue", "Low"),
    ("How can I change my account email?", "Account Issue", "Low"),
    ("I need help updating my profile information.", "Account Issue", "Low"),
    ("How do I change my account password?", "Account Issue", "Low"),
    ("I cannot update my phone number.", "Account Issue", "Medium"),
    ("My account information is not saving.", "Account Issue", "Medium"),
    ("I am unable to change my email address.", "Account Issue", "Medium"),
    ("My profile changes are not being saved.", "Account Issue", "Medium"),
    ("I cannot access my account after changing my password.", "Account Issue", "Medium"),
    ("Someone tried to access my account.", "Account Issue", "High"),
    ("I think someone has hacked my account.", "Account Issue", "High"),
    ("There is suspicious activity on my account.", "Account Issue", "High"),
    ("My account was accessed by someone else.", "Account Issue", "High"),
    ("I received an alert about an unknown login.", "Account Issue", "High"),
    ("Someone changed my account details without permission.", "Account Issue", "High"),
    ("I cannot log into my account.", "Account Issue", "Medium"),
    ("My account is locked.", "Account Issue", "Medium"),
    ("I need to recover my account.", "Account Issue", "Medium"),
    ("My login credentials are not working.", "Account Issue", "Medium"),
    ("How do I reset my password?", "Account Issue", "Low"),
    ("Can I change the email linked to my account?", "Account Issue", "Low"),
    ("I want to update my profile.", "Account Issue", "Low"),
    ("I forgot my login password.", "Account Issue", "Low"),
    ("Where can I change my username?", "Account Issue", "Low"),
    ("My account has been locked unexpectedly.", "Account Issue", "Medium"),
    ("The verification code is not working.", "Account Issue", "Medium"),
    ("I am not receiving the account verification code.", "Account Issue", "Medium"),
    ("My account login keeps failing.", "Account Issue", "Medium"),
    ("I cannot sign into my account from my phone.", "Account Issue", "Medium"),

    # Extra Account - Medium
    ("I am having trouble logging into my account.", "Account Issue", "Medium"),
    ("My account verification is taking too long.", "Account Issue", "Medium"),
    ("I cannot update my account information.", "Account Issue", "Medium"),

    # =========================
    # PAYMENT ISSUES
    # =========================

    ("I was charged twice for the same order.", "Payment Issue", "High"),
    ("My payment failed but the money was deducted.", "Payment Issue", "High"),
    ("My card was charged but the transaction failed.", "Payment Issue", "High"),
    ("Money was deducted even though payment failed.", "Payment Issue", "High"),
    ("I was charged twice for one purchase.", "Payment Issue", "High"),
    ("The payment failed but I was still charged.", "Payment Issue", "High"),
    ("My bank account was charged but the order failed.", "Payment Issue", "High"),
    ("I see an extra charge on my account.", "Payment Issue", "Medium"),
    ("I don't understand this charge on my bill.", "Payment Issue", "Medium"),
    ("There is an unfamiliar charge on my statement.", "Payment Issue", "Medium"),
    ("Why was I charged this amount?", "Payment Issue", "Medium"),
    ("The payment amount looks incorrect.", "Payment Issue", "Medium"),
    ("My payment is still processing.", "Payment Issue", "Medium"),
    ("The transaction is showing as pending.", "Payment Issue", "Medium"),
    ("My card payment is pending.", "Payment Issue", "Medium"),
    ("Why is my payment pending?", "Payment Issue", "Medium"),
    ("Can I use another payment method?", "Payment Issue", "Low"),
    ("What payment methods do you accept?", "Payment Issue", "Low"),
    ("Can I pay using another card?", "Payment Issue", "Low"),
    ("How can I change my payment method?", "Payment Issue", "Low"),
    ("Do you accept online payments?", "Payment Issue", "Low"),
    ("Can I use a different card?", "Payment Issue", "Low"),
    ("How do I make a payment?", "Payment Issue", "Low"),
    ("Which payment options are available?", "Payment Issue", "Low"),
    ("Can I use a debit card?", "Payment Issue", "Low"),
    ("My payment was declined.", "Payment Issue", "High"),
    ("My card was declined during checkout.", "Payment Issue", "High"),
    ("The transaction failed during checkout.", "Payment Issue", "High"),
    ("My payment keeps failing.", "Payment Issue", "High"),
    ("I cannot complete my payment.", "Payment Issue", "High"),

    # Extra Payment examples
    ("My bank account was charged but the payment failed.", "Payment Issue", "High"),
    ("Money was deducted from my bank account but payment failed.", "Payment Issue", "High"),
    ("My account was charged even though the payment did not go through.", "Payment Issue", "High"),
    ("The order failed but my card was charged.", "Payment Issue", "High"),
    ("I was charged but my purchase was unsuccessful.", "Payment Issue", "High"),

    # Extra Payment - Medium
    ("My payment is still pending.", "Payment Issue", "Medium"),
    ("The payment is taking longer than expected.", "Payment Issue", "Medium"),
    ("My card payment has not completed yet.", "Payment Issue", "Medium"),

    # =========================
    # ORDER ISSUES
    # =========================

    ("Where is my order? It was supposed to arrive yesterday.", "Order Issue", "Medium"),
    ("My order has not arrived.", "Order Issue", "Medium"),
    ("My package is arriving later than expected.", "Order Issue", "Medium"),
    ("My delivery is delayed.", "Order Issue", "Medium"),
    ("The order is taking longer than expected.", "Order Issue", "Medium"),
    ("My package has been delayed.", "Order Issue", "Medium"),
    ("The delivery date has passed.", "Order Issue", "High"),
    ("My order is two weeks late.", "Order Issue", "High"),
    ("My package has not arrived after two weeks.", "Order Issue", "High"),
    ("My order is extremely delayed.", "Order Issue", "High"),
    ("I have been waiting for my order for a long time.", "Order Issue", "High"),
    ("My package has been missing for several days.", "Order Issue", "High"),
    ("I received the wrong product.", "Order Issue", "High"),
    ("The wrong item was delivered.", "Order Issue", "High"),
    ("My order contains the wrong product.", "Order Issue", "High"),
    ("I received an incorrect item.", "Order Issue", "High"),
    ("My order was cancelled unexpectedly.", "Order Issue", "High"),
    ("My order was cancelled without my permission.", "Order Issue", "High"),
    ("Why was my order cancelled?", "Order Issue", "High"),
    ("My order was cancelled automatically.", "Order Issue", "High"),
    ("How can I track my order?", "Order Issue", "Low"),
    ("Where can I find my tracking information?", "Order Issue", "Low"),
    ("Can I track my package?", "Order Issue", "Low"),
    ("I want to check my delivery status.", "Order Issue", "Low"),
    ("How do I track my shipment?", "Order Issue", "Low"),
    ("Where is my tracking number?", "Order Issue", "Low"),
    ("Can you tell me where my package is?", "Order Issue", "Low"),
    ("When will my order arrive?", "Order Issue", "Low"),
    ("How long does delivery take?", "Order Issue", "Low"),
    ("What is the expected delivery date?", "Order Issue", "Low"),

    # Extra Order - Medium
    ("My delivery is one day late.", "Order Issue", "Medium"),
    ("My package is delayed by a few days.", "Order Issue", "Medium"),
    ("My order is taking longer than expected.", "Order Issue", "Medium"),

    # =========================
    # REFUND ISSUES
    # =========================

    ("How do I request a refund?", "Refund Issue", "Low"),
    ("Can I get a refund?", "Refund Issue", "Low"),
    ("I want to request a refund.", "Refund Issue", "Low"),
    ("How can I get my money back?", "Refund Issue", "Low"),
    ("What is the refund process?", "Refund Issue", "Low"),
    ("How do refunds work?", "Refund Issue", "Low"),
    ("I requested a refund yesterday.", "Refund Issue", "Medium"),
    ("I haven't received my refund after three days.", "Refund Issue", "Medium"),
    ("My refund is still processing.", "Refund Issue", "Medium"),
    ("When will my refund arrive?", "Refund Issue", "Medium"),
    ("How long does a refund take?", "Refund Issue", "Medium"),
    ("I am waiting for my refund.", "Refund Issue", "Medium"),
    ("My refund has not arrived after a week.", "Refund Issue", "Medium"),
    ("I requested a refund several days ago.", "Refund Issue", "Medium"),
    ("My refund is delayed.", "Refund Issue", "Medium"),
    ("The refund hasn't arrived after 15 days.", "Refund Issue", "High"),
    ("My refund has been missing for a month.", "Refund Issue", "High"),
    ("I have been waiting for my refund for weeks.", "Refund Issue", "High"),
    ("My refund is overdue.", "Refund Issue", "High"),
    ("I still haven't received my money back after a month.", "Refund Issue", "High"),
    ("My refund has not arrived after several weeks.", "Refund Issue", "High"),
    ("Where is my refund after 30 days?", "Refund Issue", "High"),
    ("I have been waiting too long for my refund.", "Refund Issue", "High"),
    ("My refund is missing.", "Refund Issue", "High"),
    ("Can I get a refund for my cancelled order?", "Refund Issue", "Medium"),
    ("I need a refund for a cancelled order.", "Refund Issue", "Medium"),
    ("How do I get my money back for a cancelled order?", "Refund Issue", "Medium"),
    ("I want to cancel and request a refund.", "Refund Issue", "Medium"),
    ("Can I request a refund for my purchase?", "Refund Issue", "Low"),
    ("I want to know the refund policy.", "Refund Issue", "Low"),

    # Extra Refund examples
    ("My refund has not arrived after 20 days.", "Refund Issue", "High"),
    ("I have been waiting 30 days for my refund.", "Refund Issue", "High"),
    ("My refund is still missing after 30 days.", "Refund Issue", "High"),
    ("I haven't received my refund after several weeks.", "Refund Issue", "High"),
    ("My refund is overdue by several weeks.", "Refund Issue", "High"),

    # Extra Refund - Medium
    ("I requested a refund a few days ago.", "Refund Issue", "Medium"),
    ("My refund is taking longer than expected.", "Refund Issue", "Medium"),
    ("I am still waiting for my refund.", "Refund Issue", "Medium"),

    # =========================
    # TECHNICAL ISSUES
    # =========================

    ("The application crashes whenever I open it.", "Technical Issue", "Medium"),
    ("The app shows a blank screen.", "Technical Issue", "Medium"),
    ("The website is loading very slowly.", "Technical Issue", "Low"),
    ("The website keeps displaying an error message.", "Technical Issue", "Medium"),
    ("The app stopped working after the latest update.", "Technical Issue", "Medium"),
    ("The application is running slowly.", "Technical Issue", "Low"),
    ("The website takes too long to load.", "Technical Issue", "Low"),
    ("The app is freezing.", "Technical Issue", "Medium"),
    ("The screen becomes unresponsive.", "Technical Issue", "Medium"),
    ("The website is showing an error.", "Technical Issue", "Medium"),
    ("I cannot open the application.", "Technical Issue", "High"),
    ("The website is completely down.", "Technical Issue", "High"),
    ("I cannot access the website at all.", "Technical Issue", "High"),
    ("The app will not start.", "Technical Issue", "High"),
    ("The application crashes every time I open it.", "Technical Issue", "High"),
    ("The login page is not working.", "Technical Issue", "High"),
    ("The entire website is unavailable.", "Technical Issue", "High"),
    ("The app is completely unusable.", "Technical Issue", "High"),
    ("I cannot use the application at all.", "Technical Issue", "High"),
    ("The website has stopped working.", "Technical Issue", "High"),
    ("The app takes a long time to respond.", "Technical Issue", "Low"),
    ("Some pages are loading slowly.", "Technical Issue", "Low"),
    ("The website response is slow.", "Technical Issue", "Low"),
    ("The app is a little slow.", "Technical Issue", "Low"),
    ("The page is taking too long to load.", "Technical Issue", "Low"),
    ("The website sometimes shows errors.", "Technical Issue", "Medium"),
    ("I keep getting an error on the website.", "Technical Issue", "Medium"),
    ("The app displays an error message.", "Technical Issue", "Medium"),
    ("The application has stopped responding.", "Technical Issue", "Medium"),
    ("The website is not responding properly.", "Technical Issue", "Medium"),

    # Extra Technical - Medium
    ("The app sometimes freezes.", "Technical Issue", "Medium"),
    ("The website occasionally shows an error.", "Technical Issue", "Medium"),
    ("The application is having occasional problems.", "Technical Issue", "Medium"),
]


# ==========================================
# CREATE DATAFRAME
# ==========================================

df = pd.DataFrame(
    tickets,
    columns=["message", "category", "priority"]
)


# ==========================================
# ADD ID
# ==========================================

df.insert(
    0,
    "id",
    range(1, len(df) + 1)
)


# ==========================================
# SAVE DATASET
# ==========================================

df.to_csv(
    "data/tickets.csv",
    index=False
)


# ==========================================
# DISPLAY DATASET INFORMATION
# ==========================================

print("Dataset created successfully!")

print("Total tickets:", len(df))

print("\nCategory distribution:")

print(
    df["category"].value_counts()
)

print("\nPriority distribution:")

print(
    df["priority"].value_counts()
)
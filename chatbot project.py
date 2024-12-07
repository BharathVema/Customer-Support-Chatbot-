from nltk.chat.util import Chat, reflections

#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*) your name ?",
        ["My name is Customer support chatbot, but you can just call me robot.",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    #1.	Cancel order:-
    [
        r"(.*) (canceling|cancel|information) (.*) order(.*)",
        ["You can typically cancel your last order through your account settings look for a Cancel Order option in your order history or you can contact our customer support.",]
        
    ],
    [
        r"(.*) (help|assistance) (.*) order(.*)",
        ["Yes! Please provide your order number, and I can guide you through the process.",]
    ],
    [
        r"(.*) (problems|issue) (.*) order (.*)",
        ["Can you specify the issue you’re facing? I’m here to help!",]
    ],
    [
        r"(.*) (do not|don't) want (.*) order(.*)",
        ["If you don’t want the order, you can cancel it. Let me know if you need assistance!",]
    ],
    [
        r"(.*) question (.*) order(.*)",
        ["Feel free to ask your specific questions, and I’ll do my best to provide answers! ",]
    ],
    [
        r"(.*) (can't|cannot) pay (.*)",
        ["If you’re unable to pay, you may want to consider canceling the order. Let me know if you need help with that.",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    #2.	Changing order:-
    [
    r"(.*) (add|include|change|remove|missed) (.*) order(.*)",
    ["Please check if there’s an option in your order history to modify your order , or reach out to customer service for help..",]
    ],
    [
    r"(.*) (possible) (.*) (track) (.*) (ETA|order)(.*)", 
    ["Yes, you can track your last order by going to our website and using the Order Tracking feature. Just input your order number to get the latest information.",]
    ],
    [
    r"(.*) possible (.*) order(.*)",
    ["Yes,You can usually modify your order through your account settings or by contacting customer service.",]
    ],
    [
    r"(.*) items (.*) purchased (.*) want(.*)",
    ["Apology for delevering wrong items Please provide your order number, and I can guide you through the process for placing return order option. ",]
    ],
    [
    r"(.*) wrong (.*) purchased(.*)",
    ["Please provide your order number,so that we can check the product status and change the order if order is not shipped",]
    ],
    #3.	Change shipping address and setup shipping address
    [
    r"(.*) error correcting (.*) address(.*)",
    ["Please provide the correct address, and I'll guide you through the steps to update it.",]
    ],
    [
    r"(.*) (help|assistance) (.*) address(.*)",
    ["You can usually update your address in your account settings or during the checkout process. Let me know if you need specific instructions.",]
    ],
    [
    r"(.*) (problems|issue) (.*) address(.*)",
    ["Can you specify the issue you’re facing? I’m here to help!",]
    ],
    [
    r"(.*) address (.*) mistake(.*)",
    ["You can usually update your address in your account settings or by contacting customer support directly.",]
    ],
    [
    r"(.*) (edit|change|update) (.*) address(.*)",
    ["Please check your account settings for the shipping address section, or let me know what platform you're using for more specific help. ",]
    ],
    [
    r"(.*) address (.*) (edit|change|update) (.*)",
    ["Please check your account settings for the shipping address section, or let me know what platform you're using for more specific help. ",]
    ],
    [
    r"(.*) address (edit|change|update)",
    ["Please check your account settings for the shipping address section, or let me know what platform you're using for more specific help. ",]
    ],
    [
    r"(.*) set (.*) (another|different|new) (.*) address(.*)",
    ["Go to your account settings, select Shipping Addresses, and choose Add New Address Enter the details and save.",]
    ],
    [
    r"set (.*) (another|different|new) (.*) address(.*)",
    ["Go to your account settings, select Shipping Addresses, and choose Add New Address Enter the details and save.",]
    ],
    [
    r"(.*) wrong (.*)", 
    ["Contact customer support directly if the order has already been placed. They can often assist with corrections.",]
    ],
    #.Check cancellation fee
    [
    r"(.*) (assistance|help) (.*) (fee|fees|penality|charge)(.*)", 
    ["Yes! Please provide the name of the service or contract, and I can help you find the cancellation fee details.",]
    ],
    [
    r"(.*) show (.*) (fee|fees|penality|charge)(.*)", 
    ["You can typically find this information in the terms and conditions of your contract or by checking the customer service section of the company’s website.",]
    ],
    [
    r"(.*) (breaking|broke) (.*)", 
    ["The charge for breaking a contract varies. Please refer to your specific contract terms or contact customer support for the exact fee.",]
    ],
    [
    r"(.*) what (.*) early exit (.*)", 
    ["Early exit fees vary by company and service. They are typically outlined in your contract or terms of service.",]
    ],
    [
    r"(.*) (check|show|see|seeing|find|finding|exit) (.*) (fee|fees|penality|charge)(.*)", 
    ["Look for cancellation policy information in your account or on the company’s official website under customer support.",]
    ],
    [
    r"(.*) termination (fee|fees|penality|charge)(.*)", 
    ["These charges are typically included in the terms of service. If you need assistance, contacting customer support can provide clarity.",]
    ],
    #Check invoice
    [
    r"(.*) (assistance|help) (.*) (invoice|invoices)(.*)", 
    ["You can usually access your invoices through your account dashboard. Look for a section labeled Invoices, Billing, or Order History. If you need specific months, let me know which ones!",]
    ],
    [
    r"(.*) (find|finding|check|checking|look|looking|show) (.*) (invoice|invoices)(.*)", 
    ["If you’re unsure how to find your invoices, here’s a general guide:Log into your account.Navigate to the Billing, Invoices, or Order History section.Look for the desired month or purchase date.Click on the invoice link to view or download it.",]
    ],
    [
    r"(assistance|help) (.*) (invoice|invoices)(.*)", 
    ["You can usually access your invoices through your account dashboard. Look for a section labeled Invoices, Billing, or Order History. If you need specific months, let me know which ones!",]
    ],
    [
    r"(find|finding|check|checking|look|looking|show) (.*) (invoice|invoices)(.*)", 
    ["If you’re unsure how to find your invoices, here’s a general guide:Log into your account.Navigate to the Billing, Invoices, or Order History section.Look for the desired month or purchase date.Click on the invoice link to view or download it.",]
    ],
    #place order
    [
    r"(buy|buying|purchase|make|possible) (.*) (item|items|something|order)(.*)", 
    ["To make a purchase, follow these steps:Visit our website and browse the items you’re interested in.Click on the item to view details, then select any options (like size or color).Click “Add to Cart,” then proceed to checkout when you’re ready.Follow the prompts to enter your shipping and payment information, then confirm your order. If you have any questions along the way, just let us know!",]
    ],
    [
    r"(assistance|help) (.*) (buy|buying|purchase)(.*)", 
    ["Sure,If you need help with purchasing items, feel free to reach out! We can guide you through the process of selecting and buying what you need.",]
    ],
    [
    r"(.*) (buy|buying|purchase|make|possible) (.*) (item|items|something|order)(.*)", 
    ["To make a purchase, follow these steps:Visit our website and browse the items you’re interested in.Click on the item to view details, then select any options (like size or color).Click “Add to Cart,” then proceed to checkout when you’re ready.Follow the prompts to enter your shipping and payment information, then confirm your order. If you have any questions along the way, just let us know!",]
    ],
    [
    r"(.*) (assistance|help) (.*) (buy|buying|purchase)(.*)", 
    ["Sure,If you need help with purchasing items, feel free to reach out! We can guide you through the process of selecting and buying what you need.",]
    ],
    [
    r"(.*) (make|possible) (.*) (purchase)(.*)", 
    ["To make a purchase, follow these steps:Visit our website and browse the items you’re interested in.Click on the item to view details, then select any options (like size or color).Click “Add to Cart,” then proceed to checkout when you’re ready.Follow the prompts to enter your shipping and payment information, then confirm your order. If you have any questions along the way, just let us know!",]
    ],
    [
    r"(make|possible) (purchase)(.*)", 
    ["To make a purchase, follow these steps:Visit our website and browse the items you’re interested in.Click on the item to view details, then select any options (like size or color).Click “Add to Cart,” then proceed to checkout when you’re ready.Follow the prompts to enter your shipping and payment information, then confirm your order. If you have any questions along the way, just let us know!",]
    ],
    [
    r"(buy|buying|purchase|make|possible) (.*) (item|items|something|order)(.*)", 
    ["To make a purchase, follow these steps:Visit our website and browse the items you’re interested in.Click on the item to view details, then select any options (like size or color).Click “Add to Cart,” then proceed to checkout when you’re ready.Follow the prompts to enter your shipping and payment information, then confirm your order. If you have any questions along the way, just let us know!",]
    ],
    [
    r"(assistance|help) (.*) (buy|buying|purchase)(.*)", 
    ["Sure,If you need help with purchasing items, feel free to reach out! We can guide you through the process of selecting and buying what you need.",]
    ],
    #track order
    [
    r"(.*) (check|track|checking|tracking|show|status|where) (.*) (ETA|order|orders)(.*)", 
    ["You can check the status of your order by visiting our website and navigating to the Order Tracking section. Enter your order number and email address to see the current status.",]
    ],
    [
    r"(.*) (assistance|help) (.*) (ETA|order|orders)(.*)", 
    ["Of course! Please provide your order number, and I can help you track it.",]
    ],
    [
    r"(check|track|checking|tracking|show|status|where) (.*) (ETA|order|orders)(.*)", 
    ["You can check the status of your order by visiting our website and navigating to the Order Tracking section. Enter your order number and email address to see the current status.",]
    ],
    [
    r"(assistance|help) (.*) (ETA|order|orders)(.*)", 
    ["Of course! Please provide your order number, and I can help you track it.",]
    ],
    #get invoice
    [
    r"(get|getting) (invoice|invoices)(.*)", 
    ["If you're uncertain about how to obtain invoices, here’s a quick guide:Log in to your account.Navigate to the “Order History” or “Invoices” section.Select the relevant order, and there should be an option to download or view the invoice. If you have any trouble, please reach out for further assistance!",]
    ],
    [
    r"(help|assistance) (invoice|invoices)(.*)", 
    ["If you need invoices from specific months or month, please provide your account details and the purchase dates, and we'll retrieve them for you.",]
    ],
    [
    r"(.*) (get|getting) (.*) (invoice|invoices)(.*)", 
    ["If you're uncertain about how to obtain invoices, here’s a quick guide:Log in to your account.Navigate to the “Order History” or “Invoices” section.Select the relevant order, and there should be an option to download or view the invoice. If you have any trouble, please reach out for further assistance!",]
    ],
    [
    r"(.*) (help|assistance) (.*) (invoice|invoices)(.*)", 
    ["If you need invoices from specific months or month, please provide your account details and the purchase dates, and we'll retrieve them for you.",]
    ],
    #payment issues
    [
    r"(.*)(help|assistance) (.*) payment (method|methods|option|options)(.*)", 
    ["Go to the website where you want to make a payment. Often, services list their accepted payment methods during the checkout process or in the FAQ or Payment Options section.If you can't find payment details on the website, you can always reach out to the customer support team via email, chat, or phone to inquire about accepted payment methods.",]
    ],
    [
    r"(help|assistance) (.*) payment (method|methods|option|options)(.*)", 
    ["Go to the website where you want to make a payment. Often, services list their accepted payment methods during the checkout process or in the FAQ or Payment Options section.If you can't find payment details on the website, you can always reach out to the customer support team via email, chat, or phone to inquire about accepted payment methods.",]
    ],
    [
    r"(.*) (help|assistance) (.*) (payment|payments) (.*)", 
    ["If you need help reporting a payment issue, please contact our customer support team directly. You can reach them through our support page or by email, and they’ll guide you through the process.",]
    ],
    [
    r"(help|assistance) (.*) (payment|payments)(.*)", 
    ["If you need help reporting a payment issue, please contact our customer support team directly. You can reach them through our support page or by email, and they’ll guide you through the process.",]
    ],
    [
    r"(.*) (help|assistance) (payment|payments)(.*)", 
    ["If you need help reporting a payment issue, please contact our customer support team directly. You can reach them through our support page or by email, and they’ll guide you through the process.",]
    ],
    [
    r"(.*)(help|assistance) (.*) (payment|payments)(.*)", 
    ["If you need help reporting a payment issue, please contact our customer support team directly. You can reach them through our support page or by email, and they’ll guide you through the process.",]
    ],
    [
    r"(.*) (report|reporting|solve|solving) (.*) (payment|payments)(.*)", 
    ["To report a payment issue, follow these steps:Go to our website and navigate to the “Support” or “Help” section.Look for the “Report Payment Issues” link.Fill out the form with details about your issue and submit it. If you need further assistance, feel free to ask!",]
    ],
    [
    r"(report|reporting|solve|solving) (.*) (payment|payments)", 
    ["To report a payment issue, follow these steps:Go to our website and navigate to the “Support” or “Help” section.Look for the “Report Payment Issues” link.Fill out the form with details about your issue and submit it. If you need further assistance, feel free to ask!",]
    ],
    [
    r"(.*) (report|reporting|solve|solving) (payment|payments)(.*)", 
    ["To report a payment issue, follow these steps:Go to our website and navigate to the “Support” or “Help” section.Look for the “Report Payment Issues” link.Fill out the form with details about your issue and submit it. If you need further assistance, feel free to ask!",]
    ],
    [
    r"(report|reporting|solve|solving) (payment|payments)(.*)", 
    ["To report a payment issue, follow these steps:Go to our website and navigate to the “Support” or “Help” section.Look for the “Report Payment Issues” link.Fill out the form with details about your issue and submit it. If you need further assistance, feel free to ask!",]
    ],
    #PAYMENT METHODS
    [
    r"(.*) (check|checking|list|listing|see|seeing|show) (.*) payment (method|methods|option|options)(.*)", 
    ["These are typically the payment methods that online services or businesses accept:Credit and Debit Cards:Visa, MasterCard, American Express, Discover, etc.;Digital Wallets:PayPal, Apple Pay, Google Pay, Samsung Pay, etc.;Bank Transfers:ACH, SEPA (Europe), wire transfers, etc.;Cryptocurrency:Bitcoin, Ethereum, etc. (depending on the service).;Other Options:Prepaid cards, direct billing, etc.",]
    ],
    [
    r"(check|checking|list|listing|see|seeing|show) (.*) payment (method|methods|option|options)(.*)", 
    ["These are typically the payment methods that online services or businesses accept:Credit and Debit Cards:Visa, MasterCard, American Express, Discover, etc.;Digital Wallets:PayPal, Apple Pay, Google Pay, Samsung Pay, etc.;Bank Transfers:ACH, SEPA (Europe), wire transfers, etc.;Cryptocurrency:Bitcoin, Ethereum, etc. (depending on the service).;Other Options:Prepaid cards, direct billing, etc.",]
    ],
    [
    r"what (.*) (allowed|accepted) payment (method|methods|option|options)(.*)", 
    ["These are typically the payment methods that online services or businesses accept:Credit and Debit Cards:Visa, MasterCard, American Express, Discover, etc.;Digital Wallets:PayPal, Apple Pay, Google Pay, Samsung Pay, etc.;Bank Transfers:ACH, SEPA (Europe), wire transfers, etc.;Cryptocurrency:Bitcoin, Ethereum, etc. (depending on the service).;Other Options:Prepaid cards, direct billing, etc.",]
    ],
    [
    r"what (.*) payment (method|methods|option|options) (.*) (allowed|accepted)", 
    ["These are typically the payment methods that online services or businesses accept:Credit and Debit Cards:Visa, MasterCard, American Express, Discover, etc.;Digital Wallets:PayPal, Apple Pay, Google Pay, Samsung Pay, etc.;Bank Transfers:ACH, SEPA (Europe), wire transfers, etc.;Cryptocurrency:Bitcoin, Ethereum, etc. (depending on the service).;Other Options:Prepaid cards, direct billing, etc.",]
    ],
    [
    r"(.*) (amex|googlepay|google pay|gpay)(.*)", 
    ["yes,you can",]
    ],
    #NEWSLETTER SUBSCRIPTION
    [
    r"(.*) (assistance|help) (.*) (subscribe|signup|sign up|signing up|subscribing) (.*) newsletter(.*)", 
    ["If you're having trouble signing up, please check your email settings to ensure they’re not blocking our messages. You can also try a different browser or device. If problems persist, feel free to reach out for assistance.",]
    ],
    [
    r"(assistance|help) (.*) (subscribe|signup|sign up|signing up|subscribing) (.*) newsletter(.*)", 
    ["If you're having trouble signing up, please check your email settings to ensure they’re not blocking our messages. You can also try a different browser or device. If problems persist, feel free to reach out for assistance.",]
    ],
    [
    r"(.*) (subscribe|signup|sign up|signing up|subscribing) (.*) newsletter(.*) (assistance|help)", 
    ["If you're having trouble signing up, please check your email settings to ensure they’re not blocking our messages. You can also try a different browser or device. If problems persist, feel free to reach out for assistance.",]
    ],
    [
    r"(.*) (subscribe|signup|sign up|signing up|subscribing) (.*) newsletter(.*)", 
    ["To subscribe to our newsletter, simply visit our website and look for the newsletter sign-up section, usually found at the bottom of the homepage. Enter your email address, and you’ll start receiving updates!",]
    ],
    [
    r"(subscribe|signup|sign up|signing up|subscribing) (.*) newsletter(.*)", 
    ["To subscribe to our newsletter, simply visit our website and look for the newsletter sign-up section, usually found at the bottom of the homepage. Enter your email address, and you’ll start receiving updates!",]
    ],
    [
    r"(.*) (assistance|help) (.*) (unsubscribe|cancel|cancelling|unsubscribing) (.*) newsletter(.*)", 
    ["If you’re having issues unsubscribing, please let us know. We can manually remove you from the list or guide you through the process to ensure it’s done correctly.",]
    ],
    [
    r"(assistance|help) (.*) (unsubscribe|cancel|cancelling|unsubscribing) (.*) newsletter(.*)", 
    ["If you’re having issues unsubscribing, please let us know. We can manually remove you from the list or guide you through the process to ensure it’s done correctly.",]
    ],
    [
    r"(.*) (unsubscribe|cancel|cancelling) (.*) newsletter(.*) (assistance|help)", 
    ["If you’re having issues unsubscribing, please let us know. We can manually remove you from the list or guide you through the process to ensure it’s done correctly.",]
    ],
    [
    r"(.*) (unsubscribe|cancel|cancelling|unsubscribing) (.*) newsletter(.*)", 
    ["To cancel your newsletter subscription, look for the unsubscribe link at the bottom of any newsletter email you’ve received. If you need further help, please contact our support team, and we’ll assist you promptly.",]
    ],
    [
    r"(unsubscribe|cancel|cancelling|unsubscribing) (.*) newsletter(.*)", 
    ["To cancel your newsletter subscription, look for the unsubscribe link at the bottom of any newsletter email you’ve received. If you need further help, please contact our support team, and we’ll assist you promptly.",]
    ],
    [
    r"status (.*) newsletter(.*)", 
    ["If you’d like to check your current subscription status, please provide your email address, and we can confirm whether you’re subscribed or not.",]
    ],
    [
    r"do you have (.*) newsletter(.*)", 
    ["Yes,we do let me know it you need any help in subscription",]
    ],
    #COMPLAINTS
    [
    r"(.*) (filing|file|make|lodge) (.*) complaint(.*)", 
    ["You can file a complaint by visiting our website's Contact Us section or calling our customer service number.",]
    ],
    [
    r"(filing|file|make|lodge) (.*) complaint(.*)", 
    ["You can file a complaint by visiting our website's Contact Us section or calling our customer service number.",]
    ],
    [
    r"(.*) (filing|file|make|lodge) (.*) claim(.*)", 
    ["You can file a consumer claim by filling out our online form or contacting customer service for assistance.",]
    ],
    [
    r"(.*) (filing|file|make|lodge) (.*) reclamation(.*)", 
    ["To file a reclamation, you can submit your complaint through our online form or contact our customer service directly.",]
    ],
    [
    r"(.*) (assistance|help)(.*) complaint(.*)", 
    ["I’m here to help! Please let me know the details of your complaint.",]
    ],
    [
    r"(assistance|help)(.*) complaint(.*)", 
    ["I’m here to help! Please let me know the details of your complaint.",]
    ],
    [
    r"(.*) (assistance|help)(.*) (claim|reclaimation) (.*)", 
    ["Please provide the details of your claim, and I can guide you through the process.",]
    ],
    [
    r"(assistance|help)(.*) (claim|reclaimation) (.*)", 
    ["Please provide the details of your claim, and I can guide you through the process.",]
    ],
    #review
    [
    r"(.*) (e-mail) (.*) (feedback|review) (.*)", 
    ["You can email us at support@example.com for feedback and reviews.",]
    ],
    [
    r"(.*) (email) (.*) (feedback|review) (.*)", 
    ["You can email us at support@example.com for feedback and reviews.",]
    ],
    [
    r"(assistance|help) (.*) (review|feedback) (.*)", 
    ["Let me know which service you’d like to review, and I can guide you on how to do it.",]
    ],
    [
    r"(assistance|help) (.*) (review|feedback)", 
    ["Let me know which service you’d like to review, and I can guide you on how to do it.",]
    ],
    [
    r"(.*) (assistance|help) (.*) (review|feedback) (.*)", 
    ["Let me know which service you’d like to review, and I can guide you on how to do it.",]
    ],
    [
    r"(.*) (submitting|submit|leave|leaving) (.*) (feedback|review) (.*)", 
    ["Reviews can be submitted on our website or through platforms like Google Reviews or Yelp.",]
    ],
    [
    r"(.*) (submitting|submit|leave|leaving) (.*) (feedback|review)", 
    ["Reviews can be submitted on our website or through platforms like Google Reviews or Yelp.",]
    ],
    [
    r"(submitting|submit|leave|leaving) (feedback|review)", 
    ["Reviews can be submitted on our website or through platforms like Google Reviews or Yelp.",]
    ],
    #create account
    [
    r"(.*) (assistance|help) (.*) (register|registering|create|creating|open|opening) (.*)", 
    ["If you're having trouble:Double-check that you’ve filled out all required fields correctly.Ensure your password meets the service's requirements (length, special characters, etc.).Look for help or FAQ sections on the website for specific guidance.Don’t hesitate to contact customer support if you’re still having issues.",]
    ],
    [
    r"(.*) (assistance|help) (.*) (register|registering|create|creating|open|opening)", 
    ["If you're having trouble:Double-check that you’ve filled out all required fields correctly.Ensure your password meets the service's requirements (length, special characters, etc.).Look for help or FAQ sections on the website for specific guidance.Don’t hesitate to contact customer support if you’re still having issues.",]
    ],
    [
    r"(assistance|help) (.*) (register|registering|create|creating|open|opening)", 
    ["If you're having trouble:Double-check that you’ve filled out all required fields correctly.Ensure your password meets the service's requirements (length, special characters, etc.).Look for help or FAQ sections on the website for specific guidance.Don’t hesitate to contact customer support if you’re still having issues.",]
    ],
    [
    r"(.*) (create|creating|open|opening|register|registering) (.*) (account)", 
    ["Here’s a general step-by-step:Go to the sign-up page.Fill out the required fields (name, email, password).Agree to any terms and conditions.Verify your email if prompted (check your inbox for a verification link).Complete any additional steps as directed by the platform.",]
    ],
    [
    r"(.*) (create|creating|open|opening|register|registering) (.*) (account) (.*)", 
    ["Here’s a general step-by-step:Go to the sign-up page.Fill out the required fields (name, email, password).Agree to any terms and conditions.Verify your email if prompted (check your inbox for a verification link).Complete any additional steps as directed by the platform.",]
    ],
    [
    r"(.*) (register|registering)", 
    ["Here’s a general step-by-step:Go to the sign-up page.Fill out the required fields (name, email, password).Agree to any terms and conditions.Verify your email if prompted (check your inbox for a verification link).Complete any additional steps as directed by the platform.",]
    ],
    [
    r"(register|registering|create|creating|open|opening) (.*)", 
    ["Here’s a general step-by-step:Go to the sign-up page.Fill out the required fields (name, email, password).Agree to any terms and conditions.Verify your email if prompted (check your inbox for a verification link).Complete any additional steps as directed by the platform.",]
    ],
    [
    r"(register|registering)", 
    ["Here’s a general step-by-step:Go to the sign-up page.Fill out the required fields (name, email, password).Agree to any terms and conditions.Verify your email if prompted (check your inbox for a verification link).Complete any additional steps as directed by the platform.",]
    ],
    #delete account
    [
    r"(.*) (assistance|help) (.*) (delete|deleting|close|closing|deletion|deletions|remove|removing|temination|teminate|removal|canceling|cancel|cancelation) (.*)", 
    ["If you're experiencing issues:Ensure you’re logged into the correct account.Look for troubleshooting tips in the help section or FAQs.If the option to delete is missing, it might require contacting customer support for assistance.",]
    ],
    [
    r"(.*) (assistance|help) (.*) (delete|deleting|close|closing|deletion|deletions|remove|removing|temination|teminate|removal|canceling|cancel|cancelation) (.*)", 
    ["If you're experiencing issues:Ensure you’re logged into the correct account.Look for troubleshooting tips in the help section or FAQs.If the option to delete is missing, it might require contacting customer support for assistance.",]
    ],
    [
    r"(assistance|help) (.*) (delete|deleting|close|closing|deletion|deletions|remove|removing|temination|teminate|removal|canceling|cancel|cancelation) (.*)", 
    ["If you're experiencing issues:Ensure you’re logged into the correct account.Look for troubleshooting tips in the help section or FAQs.If the option to delete is missing, it might require contacting customer support for assistance.",]
    ],
    [
    r"(.*) (delete|deleting|close|closing|deletion|deletions|remove|removing|temination|teminate|removal|canceling|cancel|cancelation) (.*) (account)", 
    ["To delete or cancel your account:Visit the website or app where your account is located.Look for a section labeled Account Settings, Privacy, or Security.There should be an option for Delete Account, Cancel Account, or similar wording.",]
    ],
    [
    r"(.*) (delete|deleting|close|closing|deletion|deletions|remove|removing|temination|teminate|removal|canceling|cancel|cancelation) (.*) (account) (.*)", 
    ["To delete or cancel your account:Visit the website or app where your account is located.Look for a section labeled Account Settings, Privacy, or Security.There should be an option for Delete Account, Cancel Account, or similar wording.",]
    ],
    [
    r"(.*) (delete|deleting|close|closing|deletion|deletions|remove|removing|temination|teminate|removal|canceling|cancel|cancelation)", 
    ["To delete or cancel your account:Visit the website or app where your account is located.Look for a section labeled Account Settings, Privacy, or Security.There should be an option for Delete Account, Cancel Account, or similar wording.",]
    ],
    #switch account
    [
    r"(.*) (assistance|help) (.*) (account|profile|user) (.*)", 
    ["I can help! Log out from your current session and log back in with the desired user account.",]
    ],
    [
    r"(.*) (assistance|help) (account|profile|user) (.*)", 
    ["I can help! Log out from your current session and log back in with the desired user account.",]
    ],
    [
    r"(.*) (assistance|help) (.*) (account|profile|user) (.*)", 
    ["I can help! Log out from your current session and log back in with the desired user account.",]
    ],
    [
    r"(.*) (assistance|help) (.*) (account|profile|user)", 
    ["I can help! Log out from your current session and log back in with the desired user account.",]
    ],
    [
    r"(assistance|help) (.*) (account|profile|user) (.*)", 
    ["I can help! Log out from your current session and log back in with the desired user account.",]
    ],
    [
    r"(account|profile|user) (assistance|help) (.*)", 
    ["I can help! Log out from your current session and log back in with the desired user account.",]
    ],
    [
    r"(.*) (account|profile|user) (.*) (assistance|help) (.*)", 
    ["I can help! Log out from your current session and log back in with the desired user account.",]
    ],
    [
    r"(.*) (use|switch|change|changing|using|switching) (.*) (profile|account|user) (.*)", 
    ["Log out of your current account, then click on Login and enter the credentials for the other account.",]
    ],
    [
    r"(.*) (use|switch|change|changing|using|switching) (.*) (profile|account|user)", 
    ["Log out of your current account, then click on Login and enter the credentials for the other account.",]
    ],
    [
    r"(use|switch|change|changing|using|switching) (.*) (profile|account|user)", 
    ["Log out of your current account, then click on Login and enter the credentials for the other account.",]
    ],
    [
    r"(use|switch|change|changing|using|switching) (profile|account|user)", 
    ["Log out of your current account, then click on Login and enter the credentials for the other account.",]
    ],
    [
    r"(.*) (use|switch|change|changing|using|switching) (profile|account|user)", 
    ["Log out of your current account, then click on Login and enter the credentials for the other account.",]
    ],
    #edit account
    [
    r"(.*) (assistance|help) (.*) (edit|editing|change|changing|coorect|correcting|modify|modifying|update|updating) (.*)", 
    ["If you’re unsure how to make these edits:Check the website’s Help Center or FAQ section for guides on updating your information.Some platforms have tutorial videos or step-by-step instructions available.",]
    ],
    [
    r"(.*) (assistance|help) (edit|editing|change|changing|coorect|correcting|modify|modifying|update|updating) (.*)", 
    ["If you’re unsure how to make these edits:Check the website’s Help Center or FAQ section for guides on updating your information.Some platforms have tutorial videos or step-by-step instructions available.",]
    ],
    [
    r"(.*) (assistance|help) (.*) (edit|editing|change|changing|coorect|correcting|modify|modifying|update|updating) (.*)", 
    ["If you’re unsure how to make these edits:Check the website’s Help Center or FAQ section for guides on updating your information.Some platforms have tutorial videos or step-by-step instructions available.",]
    ],
    [
    r"(assistance|help) (.*) (edit|editing|change|changing|coorect|correcting|modify|modifying|update|updating) (.*)", 
    ["If you’re unsure how to make these edits:Check the website’s Help Center or FAQ section for guides on updating your information.Some platforms have tutorial videos or step-by-step instructions available.",]
    ],
    [
    r"(.*) (edit|editing|change|changing|coorect|correcting|modify|modifying|update|updating) (.*) (account|information|info|data|profile)", 
    ["To edit your personal information:Log in to your account on the website or app.Navigate to the Account Settings, Profile, or My Account section.Look for options labeled Edit Profile or Update Information.",]
    ],
    [
    r"(.*) (edit|editing|change|changing|coorect|correcting|modify|modifying|update|updating) (.*) (account|information|info|data|profile) (.*)", 
    ["To edit your personal information:Log in to your account on the website or app.Navigate to the Account Settings, Profile, or My Account section.Look for options labeled Edit Profile or Update Information.",]
    ],
    [
    r"(.*) (edit|editing|change|changing|coorect|correcting|modify|modifying|update|updating) (account|information|info|data|profile)", 
    ["To edit your personal information:Log in to your account on the website or app.Navigate to the Account Settings, Profile, or My Account section.Look for options labeled Edit Profile or Update Information.",]
    ],
    #recover password
    [
    r"(.*) (assistance|help) (.*) (pass|key|password|pwd|pin) (.*)", 
    ["I can help! Please check the recovery options provided on your account’s login page.",]
    ],
    [
    r"(.*) (assistance|help) (pass|key|password|pwd|pin) (.*)", 
    ["I can help! Please check the recovery options provided on your account’s login page.",]
    ],
    [
    r"(.*) (assistance|help) (.*) (pass|key|password|pwd|pin) (.*)", 
    ["I can help! Please check the recovery options provided on your account’s login page.",]
    ],
    [
    r"(assistance|help) (.*) (pass|key|password|pwd|pin) (.*)", 
    ["I can help! Please check the recovery options provided on your account’s login page.",]
    ],
    [
    r"(.*) (tell|information|restore|recover|retrive|reset|recovery|recovering|restoring) (.*) (pass|key|password|pwd|pin)", 
    ["Visit the login page and click on Forgot Password? Follow the instructions to reset it via your registered email or phone.",]
    ],
    [
    r"(.*) (tell|information|restore|recover|retrive|reset|recovery|recovering|restoring) (.*) (pass|key|password|pwd|pin) (.*)", 
    ["Visit the login page and click on Forgot Password? Follow the instructions to reset it via your registered email or phone.",]
    ],
    [
    r"(.*) (tell|information|restore|recover|retrive|reset|recovery|recovering|restoring) (pass|key|password|pwd|pin)", 
    ["Visit the login page and click on Forgot Password? Follow the instructions to reset it via your registered email or phone.",]
    ],
    [
    r"(tell|information|restore|recover|retrive|reset|recovery|recovering|restoring) (.*) (pass|key|password|pwd|pin)", 
    ["Visit the login page and click on Forgot Password? Follow the instructions to reset it via your registered email or phone.",]
    ],
    [
    r"(.*) (pass|key|password|pwd|pin) (tell|information|restore|recover|retrive|reset|recovery|recovering|restoring) (.*)", 
    ["Visit the login page and click on Forgot Password? Follow the instructions to reset it via your registered email or phone.",]
    ],
    [
    r"(.*) (pass|key|password|pwd|pin) (.*) (tell|information|restore|recover|retrive|reset|recovery|recovering|restoring) (.*)", 
    ["Visit the login page and click on Forgot Password? Follow the instructions to reset it via your registered email or phone.",]
    ],
    [
    r"(.*) (pass|key|password|pwd|pin) (.*) (tell|information|restore|recover|retrive|reset|recovery|recovering|restoring)", 
    ["Visit the login page and click on Forgot Password? Follow the instructions to reset it via your registered email or phone.",]
    ],
    [
    r"(.*) (forgot|forgotten) (pass|key|password|pwd|pin)", 
    ["Visit the login page and click on Forgot Password? Follow the instructions to reset it via your registered email or phone.",]
    ],
    [
    r"(forgot|forgetten) (pass|key|password|pwd|pin)", 
    ["Visit the login page and click on Forgot Password? Follow the instructions to reset it via your registered email or phone.",]
    ],
    #registration issue
    [
    r"(.*) (assistance|help) (.*) (registration|registering|signup|sign up|sign-up) (.*)", 
    ["Please provide details about the issue, and I can assist you in troubleshooting.",]
    ],
    [
    r"(.*) (assistance|help) (registration|registering|signup|sign up|sign-up) (.*)", 
    ["Please provide details about the issue, and I can assist you in troubleshooting.",]
    ],
    [
    r"(.*) (assistance|help) (.*) (registration|registering|signup|sign up|sign-up) (.*)", 
    ["Please provide details about the issue, and I can assist you in troubleshooting.",]
    ],
    [
    r"(.*) (assistance|help) (.*) (registration|registering|signup|sign up|sign-up)", 
    ["Please provide details about the issue, and I can assist you in troubleshooting.",]
    ],
    [
    r"(assistance|help) (.*) (registration|registering|signup|sign up|sign-up) (.*)", 
    ["Please provide details about the issue, and I can assist you in troubleshooting.",]
    ],
    [
    r"(registration|registering|signup|sign up|sign-up) (assistance|help) (.*)", 
    ["Please provide details about the issue, and I can assist you in troubleshooting.",]
    ],
    [
    r"(.*) (registration|registering|signup|sign up|sign-up) (.*) (assistance|help) (.*)", 
    ["Please provide details about the issue, and I can assist you in troubleshooting.",]
    ],
    [
    r"(.*) (report|reporting|notify|notifying|information|informing|issue|issues|support|problem|problems|trouble|troubles|errors) (.*) (registration|registering|signup|sign up|sign-up)", 
    ["You can report registration issues by visiting our contact page or support forum.",]
    ],
    [
    r"(.*) (report|reporting|notify|notifying|information|informing|issue|issues|support|problem|problems|trouble|troubles) (.*) (registration|registering|signup|sign up|sign-up) (.*)", 
    ["You can report registration issues by visiting our contact page or support forum.",]
    ],
    [
    r"(.*) (report|reporting|notify|notifying|information|informing|issue|issues|support|problem|problems|trouble|troubles) (registration|registering|signup|sign up|sign-up) (.*)", 
    ["You can report registration issues by visiting our contact page or support forum.",]
    ],
    [
    r"(report|reporting|notify|notifying|information|informing|issue|issues|support|problem|problems|trouble|troubles) (registration|registering|signup|sign up|sign-up) (.*)", 
    ["You can report registration issues by visiting our contact page or support forum.",]
    ],
    [
    r"(.*) (registration|registering|signup|sign up|sign-up) (report|reporting|notify|notifying|information|informing|issue|issues|support|problem|problems|trouble|troubles)", 
    ["You can report registration issues by visiting our contact page or support forum.",]
    ],
    [
    r"(.*) information (.*)",
    ["Information can typically be found in the FAQ section of the website or in your account settings. If you tell me the service, I can help find it!",]
    ],
    [
    r"(signup|sign up|registration|sign-up) (error|errors|issue|issues)",
    ["You can report registration issues by visiting our contact page or support forum.",]
    ],
    #contact customer service
    [
    r"(.*) (time|hours|speak|contact|touch|talk|call) (.*) customer (service|support|assiatance)",
    ["You can typically find customer service hours on the company’s official website, often in the “Contact Us” section.You can contact customer service via phone, email, or live chat. Details are generally provided on the company’s website.",]
    ],
    [
    r"(.*) (time|hours|speak|contact|touch|talk|call) customer (service|support|assiatance) (.*)",
    ["You can typically find customer service hours on the company’s official website, often in the “Contact Us” section.You can contact customer service via phone, email, or live chat. Details are generally provided on the company’s website.",]
    ],
    [
    r"(.*) customer (service|support|assiatance) (.*) (time|hours|speak|contact|touch|talk|call)",
    ["You can typically find customer service hours on the company’s official website, often in the “Contact Us” section.You can contact customer service via phone, email, or live chat. Details are generally provided on the company’s website.",]
    ],
    [
    r"(.*) customer (service|support|assiatance) (.*) (time|hours|speak|contact|touch|talk|call) (.*)",
    ["You can typically find customer service hours on the company’s official website, often in the “Contact Us” section.You can contact customer service via phone, email, or live chat. Details are generally provided on the company’s website.",]
    ],
    [
    r"(.*) customer (service|support|assiatance) (.*) (help|assistance)",
    ["Visit the company’s website, specifically the contact section, or reach out via social media for assistance.",]
    ],
    [
    r"(.*) customer (service|support|assiatance) (.*) (help|assistance) (.*)",
    ["Visit the company’s website, specifically the contact section, or reach out via social media for assistance.",]
    ],
    [
    r"(.*) (help|assistance) (.*) customer (service|support|assiatance)",
    ["Visit the company’s website, specifically the contact section, or reach out via social media for assistance.",]
    ],
    [
    r"(help|assistance) (.*) customer (service|support|assiatance)",
    ["Visit the company’s website, specifically the contact section, or reach out via social media for assistance.",]
    ],
    [
    r"(.*) mail (.*) customer (service|support|assiatance)",
    ["The email address for customer service is usually found on the contact page of the company’s website.",]
    ],
    #contact human agent
    [
    r"(.*) (agent|somebody|someone|person|operator) (.*) (help|assistance)",
    ["To talk to an agent, you can call customer support or initiate a live chat and request to speak with a representative.",]
    ],
    [
    r"(.*) (agent|somebody|someone|person|operator) (.*) (help|assistance) (.*)",
    ["To talk to an agent, you can call customer support or initiate a live chat and request to speak with a representative.",]
    ],
    [
    r"(.*) (help|assistance) (.*) (agent|somebody|someone|person|operator)",
    ["To talk to an agent, you can call customer support or initiate a live chat and request to speak with a representative.",]
    ],
    [
    r"(help|assistance) (.*) (agent|somebody|someone|person|operator)",
    ["To talk to an agent, you can call customer support or initiate a live chat and request to speak with a representative.",]
    ],    
    [
    r"(.*) (chat|speak|contact|touch|talk|call|contacting|talking|transfer) (.*) (agent|somebody|someone|person|operator)",
    ["You can usually reach a live agent by calling the customer service number listed on the website or using the live chat feature if available.",]
    ],
    [
    r"(.*) (chat|speak|contact|touch|talk|call|contacting|talking|transfer) (agent|somebody|someone|person|operator) (.*)",
    ["You can usually reach a live agent by calling the customer service number listed on the website or using the live chat feature if available.",]
    ],
    [
    r"(.*) (agent|somebody|someone|person|operator) (.*) (chat|speak|contact|touch|talk|call|contacting|talking|transfer)",
    ["You can usually reach a live agent by calling the customer service number listed on the website or using the live chat feature if available.",]
    ],
    [
    r"(.*) (agent|somebody|someone|person|operator) (.*) (chat|speak|contact|touch|talk|call|contacting|talking|transfer) (.*)",
    ["You can usually reach a live agent by calling the customer service number listed on the website or using the live chat feature if available.",]
    ],
    #track refund
    [
    r"(.*) refund (.*) (status|update|anything new|updates|track) (.*) (help|assistance)",
    ["I can help with that! Please provide your order number, and I’ll check the status of your refund for you.",]
    ],
    [
    r"(.*) refund (.*) (status|update|anything new|updates|track) (.*) (help|assistance) (.*)",
    ["I can help with that! Please provide your order number, and I’ll check the status of your refund for you.",]
    ],
    [
    r"(.*) (help|assistance) (.*) refund (.*) (status|update|anything new|updates) (.*)",
    ["I can help with that! Please provide your order number, and I’ll check the status of your refund for you.",]
    ],
    [
    r"(help|assistance) (.*) refund (.*) (status|update|anything new|updates|track) (.*)",
    ["I can help with that! Please provide your order number, and I’ll check the status of your refund for you.",]
    ],
    [
    r"(help|assistance) (.*) refund (status|update|anything new|updates|track)",
    ["I can help with that! Please provide your order number, and I’ll check the status of your refund for you.",]
    ],
    [
    r"(.*) (status|update|anything new|updates|track) (.*) refund (.*) (help|assistance)",
    ["I can help with that! Please provide your order number, and I’ll check the status of your refund for you.",]
    ],
    [
    r"(.*) (status|update|anything new|updates) (.*) refund (.*) (help|assistance) (.*)",
    ["I can help with that! Please provide your order number, and I’ll check the status of your refund for you.",]
    ],
    [
    r"(.*) (help|assistance) (.*) (status|update|anything new|updates) (.*) refund (.*)",
    ["I can help with that! Please provide your order number, and I’ll check the status of your refund for you.",]
    ],
    [
    r"(help|assistance) (.*) (status|update|anything new|updates) (.*) refund (.*)",
    ["I can help with that! Please provide your order number, and I’ll check the status of your refund for you.",]
    ],
    [
    r"(help|assistance) (.*) (status|update|anything new|updates) (.*) refund",
    ["I can help with that! Please provide your order number, and I’ll check the status of your refund for you.",]
    ],
    [
    r"(.*) (status|update|anything new|updates|track) (.*) (refund)",
    ["To track your refund, please visit our website’s Refund Status page and enter your order number to view the current status.",]
    ],
    [
    r"(.*) (status|update|anything new|updates|track) (refund) (.*)",
    ["To track your refund, please visit our website’s Refund Status page and enter your order number to view the current status.",]
    ],
    [
    r"(.*) (refund) (.*) (status|update|anything new|updates|track)",
    ["To track your refund, please visit our website’s Refund Status page and enter your order number to view the current status.",]
    ],
    [
    r"(.*) (refund) (.*) (status|update|anything new|updates|track) (.*)",
    ["To track your refund, please visit our website’s Refund Status page and enter your order number to view the current status.",]
    ],
    [
    r"(.*) (refund) (status|update|anything new|updates|track) (.*)",
    ["To track your refund, please visit our website’s Refund Status page and enter your order number to view the current status.",]
    ],
    [
    r"(.*) (refund) (status|update|anything new|updates|track)",
    ["To track your refund, please visit our website’s Refund Status page and enter your order number to view the current status.",]
    ],
    [
    r"(refund) (status|update|anything new|updates|track)",
    ["To track your refund, please visit our website’s Refund Status page and enter your order number to view the current status.",]
    ],
    #check refund policy
    [
    r"(help|assistance) (getting|get) (.*) (reimbuersment|rebate|refund|back|compensation|compensations|refunds)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(help|assistance) (.*) (getting|get) (.*) (reimbuersment|rebate|refund|back|compensation|compensations|refunds)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(help|assistance) (getting|get) (.*) (reimbuersment|rebate|refund|back|compensation|compensations|refunds)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(help|assistance) (getting|get) (reimbuersment|rebate|refund|back|compensation|compensations|refunds)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(help|assistance) (.*) (getting|get) (reimbuersment|rebate|refund|back|compensation|compensations|refunds)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(help|assistance) (getting|get) (reimbuersment|rebate|refund|back|compensation|compensations|refunds)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(help|assistance) (getting|get) (.*) (reimbuersment|rebate|refund|back|compensation|compensations|refunds) (.*)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(help|assistance) (.*) (getting|get) (.*) (reimbuersment|rebate|refund|back|compensation|compensations|refunds) (.*)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(help|assistance) (getting|get) (.*) (reimbuersment|rebate|refund|back|compensation|compensations|refunds) (.*)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(help|assistance) (getting|get) (reimbuersment|rebate|refund|back|compensation|compensations|refunds) (.*)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(help|assistance) (.*) (getting|get) (reimbuersment|rebate|refund|back|compensation|compensations|refunds) (.*)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(help|assistance) (getting|get) (reimbuersment|rebate|refund|back|compensation|compensations|refunds) (.*)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(.*) (help|assistance) (getting|get) (.*) (reimbuersment|rebate|refund|back|compensation|compensations|refunds) (.*)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(.*) (help|assistance) (.*) (getting|get) (.*) (reimbuersment|rebate|refund|back|compensation|compensations|refunds) (.*)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(.*) (help|assistance) (getting|get) (.*) (reimbuersment|rebate|refund|back|compensation|compensations|refunds) (.*)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(.*) (help|assistance) (getting|get) (reimbuersment|rebate|refund|back|compensation|compensations|refunds) (.*)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(.*) (help|assistance) (.*) (getting|get) (reimbuersment|rebate|refund|back|compensation|compensations|refunds) (.*)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],
    [
    r"(.*)  (help|assistance) (getting|get) (reimbuersment|rebate|refund|back|compensation|compensations|refunds) (.*)",
    ["If you're looking to get a refund but aren’t sure how to proceed, please reach out to our customer support with your order details. They can guide you through the refund request process.",]
    ],    
    [
    r"(.*) (refund|policy|back) (.*) (help|assistance)",
    ["I can help you find the refund policy! You can usually check it on the website under sections like 'Returns,' 'Refunds,' or 'Terms and Conditions.' Would you like a direct link or need help navigating the site?",]
    ],
    [
    r"(.*) (refund|policy|back) (.*) (help|assistance) (.*)",
    ["I can help you find the refund policy! You can usually check it on the website under sections like 'Returns,' 'Refunds,' or 'Terms and Conditions.' Would you like a direct link or need help navigating the site?",]
    ],
    [
    r"(.*) (help|assistance) (.*) (refund|policy|back)",
    ["I can help you find the refund policy! You can usually check it on the website under sections like 'Returns,' 'Refunds,' or 'Terms and Conditions.' Would you like a direct link or need help navigating the site?",]
    ],
    [
    r"(help|assistance) (.*) (refund|policy|back)",
    ["I can help you find the refund policy! You can usually check it on the website under sections like 'Returns,' 'Refunds,' or 'Terms and Conditions.' Would you like a direct link or need help navigating the site?",]
    ],    
    [
    r"(.*) (check|checking|show|ask|charges|long|charge) (.*) (refund|policy|back)",
    ["Typically, you can check the refund policy by visiting the website where you made the purchase, often under Terms & Conditions, Returns, or Refunds sections.If you're dealing with a service or product, check the email confirmation or account page for policy links.Refund times vary. For many companies, refunds take 3-10 business days depending on payment method and processing time. Some companies may take longer.",]
    ],
    [
    r"(check|checking|show|ask|charges|long|charge) (.*) (refund|policy|back)",
    ["Typically, you can check the refund policy by visiting the website where you made the purchase, often under Terms & Conditions, Returns, or Refunds sections.If you're dealing with a service or product, check the email confirmation or account page for policy links.Refund times vary. For many companies, refunds take 3-10 business days depending on payment method and processing time. Some companies may take longer.",]
    ],
    [
    r"(.*) (check|checking|show|long|ask|charges|long|charge) (refund|policy|back) (.*)",
    ["Typically, you can check the refund policy by visiting the website where you made the purchase, often under Terms & Conditions, Returns, or Refunds sections.If you're dealing with a service or product, check the email confirmation or account page for policy links.Refund times vary. For many companies, refunds take 3-10 business days depending on payment method and processing time. Some companies may take longer.",]
    ],
    [
    r"(.*) (refund|policy|back) (.*) (check|checking|show|long|ask|charges|charge)",
    ["Typically, you can check the refund policy by visiting the website where you made the purchase, often under Terms & Conditions, Returns, or Refunds sections.If you're dealing with a service or product, check the email confirmation or account page for policy links.Refund times vary. For many companies, refunds take 3-10 business days depending on payment method and processing time. Some companies may take longer.",]
    ],
    [
    r"(.*) (refund|policy|back) (.*) (check|checking|show|long|ask|charges|charge) (.*)",
    ["Typically, you can check the refund policy by visiting the website where you made the purchase, often under Terms & Conditions, Returns, or Refunds sections.If you're dealing with a service or product, check the email confirmation or account page for policy links.Refund times vary. For many companies, refunds take 3-10 business days depending on payment method and processing time. Some companies may take longer.",]
    ],
    #get refund
    [
    r"(.*) (get|getting|want|need|demand|expect|receive|receiving|ask) (.*) (refund|refunds|back|rebate|reimbersment|compensation|compensations)",
    ["To request a refund, follow these steps:Visit the “Returns” or “Refunds” section on our website.Fill out the refund request form with your order number and reason for the refund.Submit the form, and you should receive a confirmation email shortly. If you need further assistance, don’t hesitate to ask!",]
    ],
    [
    r"(.*) (get|getting|want|need|demand|expect|receive|receiving|ask) (.*) (refund|refunds|back|rebate|reimbersment|compensation|compensations) (.*)",
    ["To request a refund, follow these steps:Visit the “Returns” or “Refunds” section on our website.Fill out the refund request form with your order number and reason for the refund.Submit the form, and you should receive a confirmation email shortly. If you need further assistance, don’t hesitate to ask!",]
    ],
    [
    r"(.*) (get|getting|want|need|demand|expect|receive|receiving|ask) (refund|refunds|back|rebate|reimbersment|compensation|compensations)",
    ["To request a refund, follow these steps:Visit the “Returns” or “Refunds” section on our website.Fill out the refund request form with your order number and reason for the refund.Submit the form, and you should receive a confirmation email shortly. If you need further assistance, don’t hesitate to ask!",]
    ],
    [
    r"(.*) (get|getting|want|need|demand|expect|receive|receiving|ask) (refund|refunds|back|rebate|reimbersment|compensation|compensations) (.*)",
    ["To request a refund, follow these steps:Visit the “Returns” or “Refunds” section on our website.Fill out the refund request form with your order number and reason for the refund.Submit the form, and you should receive a confirmation email shortly. If you need further assistance, don’t hesitate to ask!",]
    ],
    [
    r"(get|getting|want|need|demand|expect|receive|receiving|ask) (refund|refunds|back|rebate|reimbersment|compensation|compensations)",
    ["To request a refund, follow these steps:Visit the “Returns” or “Refunds” section on our website.Fill out the refund request form with your order number and reason for the refund.Submit the form, and you should receive a confirmation email shortly. If you need further assistance, don’t hesitate to ask!",]
    ],
    #delivery options
    [
    r"(help|assistance|problem|problems) (.*) (option|options)",
    ["If you need further help:Contact customer support via chat, email, or phone for personalized assistance.Many websites have a live chat feature that can provide immediate answers.",]
    ],
    [
    r"(help|assistance|problem|problems) (.*) (option|options) (.*)",
    ["If you need further help:Contact customer support via chat, email, or phone for personalized assistance.Many websites have a live chat feature that can provide immediate answers.",]
    ],
    [
    r"(.*) (help|assistance|problem|problems) (.*) (option|options)",
    ["If you need further help:Contact customer support via chat, email, or phone for personalized assistance.Many websites have a live chat feature that can provide immediate answers.",]
    ],
    [
    r"(.*) (help|assistance|problem|problems) (.*) (option|options) (.*)",
    ["If you need further help:Contact customer support via chat, email, or phone for personalized assistance.Many websites have a live chat feature that can provide immediate answers.",]
    ],
    [
    r"(.*) (check|checking|show|look) (.*) (option|options)",
    ["To find out what delivery options are available:Visit the website or app of the service you're using.Look for sections like “Shipping Information,” “Delivery Options,” or “Checkout” during the ordering process.Sometimes this information is also found in the FAQs.",]
    ],
    [
    r"(.*) (check|checking|show|look) (.*) (option|options) (.*)",
    ["To find out what delivery options are available:Visit the website or app of the service you're using.Look for sections like “Shipping Information,” “Delivery Options,” or “Checkout” during the ordering process.Sometimes this information is also found in the FAQs.",]
    ],
    [
    r"(.*) (about|offer|available|looking) (.*) (option|options) (.*)",
    ["Common types of delivery options include:Standard Shipping: Usually the most economical option, with longer delivery times.Express Delivery: Faster shipping for an additional fee, often delivered within 1-3 days.Same-Day Delivery: Available in some areas for urgent needs.In-Store Pickup: Order online and pick up at a local store.",]
    ],
    [
    r"(.*) (about|offer|available|looking) (.*) (option|options)",
    ["Common types of delivery options include:Standard Shipping: Usually the most economical option, with longer delivery times.Express Delivery: Faster shipping for an additional fee, often delivered within 1-3 days.Same-Day Delivery: Available in some areas for urgent needs.In-Store Pickup: Order online and pick up at a local store.",]
    ],
    [
    r"(.*) (option|options) (.*) (about|offer|available|looking)",
    ["Common types of delivery options include:Standard Shipping: Usually the most economical option, with longer delivery times.Express Delivery: Faster shipping for an additional fee, often delivered within 1-3 days.Same-Day Delivery: Available in some areas for urgent needs.In-Store Pickup: Order online and pick up at a local store.",]
    ],
    [
    r"(.*) (option|options)", 
    ["To find out what delivery options are available:Visit the website or app of the service you're using.Look for sections like “Shipping Information,” “Delivery Options,” or “Checkout” during the ordering process.Sometimes this information is also found in the FAQs.",]
    ],
    #delivery period
    [
    r"(.*) (help|assistance) (.*) (arrive|delivery|takes|take|expect|period|periods)", 
    ["If you need help Reach out via chat, email, or phone to ask about your delivery.Provide your order number for quicker assistance.",]
    ],
    [
    r"(help|assistance) (.*) (arrive|delivery|takes|take|expect|period|periods)", 
    ["If you need help Reach out via chat, email, or phone to ask about your delivery.Provide your order number for quicker assistance.",]
    ],
    [
    r"(help|assistance) (.*) (arrive|delivery|takes|take|expect|period|periods) (.*)", 
    ["If you need help Reach out via chat, email, or phone to ask about your delivery.Provide your order number for quicker assistance.",]
    ],
    [
    r"(.*) (check|checking|soon|show) (.*) (arrive|long|expect|period|periods|take|takes) (.*)", 
    ["Track Your Order: Look for a “Track Order” link on the website or in your order confirmation email.Account Login: If you have an account, log in and navigate to your order history for details on delivery times.",]
    ],
    [
    r"(.*) (check|checking|soon|show) (.*) (arrive|long|expect|period|periods|take|takes)", 
    ["Track Your Order: Look for a “Track Order” link on the website or in your order confirmation email.Account Login: If you have an account, log in and navigate to your order history for details on delivery times.",]
    ],
    [
    r"(.*) (about|find|looking|look|long) (.*) (period|periods|take|takes)", 
    ["Delivery timeframes typically vary:Standard Delivery: Usually takes 3-7 business days.Express Delivery: Typically arrives within 1-3 business days.Check the specific product page or during checkout for estimated delivery times.",]
    ],
    [
    r"what (.*) (arrive|long|expect|period|periods|take|takes) (.*)", 
    ["Track Your Order: Look for a “Track Order” link on the website or in your order confirmation email.Account Login: If you have an account, log in and navigate to your order history for details on delivery times.",]
    ],
    [
    r"when (.*) (arrive|long|expect|period|periods|take|takes)", 
    ["Track Your Order: Look for a “Track Order” link on the website or in your order confirmation email.Account Login: If you have an account, log in and navigate to your order history for details on delivery times.",]
    ],
    [
    r"delivery (arrive|long|expect|period|periods|take|takes)", 
    ["Track Your Order: Look for a “Track Order” link on the website or in your order confirmation email.Account Login: If you have an account, log in and navigate to your order history for details on delivery times.",]
    ],
    [
    r"(.*) (.*)", 
    ["Contact customer support for the queries thankyou",]
    ],
 
]   
#default message at the start of chat
print("Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
#Create Chat Bot
chat = Chat(pairs, reflections)


chat.converse()


customer_data_gen_prompts = """

You are a helpful assistant designed to generate banking customer data. You will be given a format for the data to generate and some examples of the data.

Generate Synthetic Customer Records Dataset with the following columns:
    - external_party_id: A randomly generated external party id. Example : CUSTR0001
    - party_id : A randomly generated party id. Example : BANK12344
    - first_name : First name of the customer: Example : John
    - last_name : Last name of the customer: Example : Doe
    - address : Address of the customer: Example : 123 Main Street, City, Country, LM02 3AB
    - products : Is an array of products which is defined below

The below is the definition of the products:
    - product_id : A randomly generated product id. Example : 3099923456789
    - product_type : Type of the product. Example : Savings Account, Current Account, Business Current Account, Business Savings Account, ISA
    - product_description : Description of the product. Example : This is a savings account.
    - external_system_id : A randomly generated external system id. Example : 1

Return 20 rows of data for the user. Your response should strictly be in the format of a valid CSV.

external_party_id,party_id,first_name,last_name,address,products
CUSTR0001,BANK12344,John,Doe,123 Main Street, City, Country, LM02 3AB,[{"product_id": 3099923456789, "product_type": "Savings Account", "product_description": "This is a savings account.", "external_system_id": 1}]
CUSTR0002,BANK12345,Jane,Doe,124 Main Street, City, Country, LM02 3AB,[{"product_id": 3099923456790, "product_type": "Current Account", "product_description": "This is a current account.", "external_system_id": 1}]
CUSTR0003,BANK12346,John,Smith,125 Main Street, City, Country, LM02 3AB,[{"product_id": 3099923456791, "product_type": "Business Current Account", "product_description": "This is a business current account.", "external_system_id": 1}]
CUSTR0004,BANK12347,Jane,Smith,126 Main Street, City, Country, LM02 3AB,[{"product_id": 3099923456792, "product_type": "Business Savings Account", "product_description": "This is a business savings account.", "external_system_id": 1}]

"""
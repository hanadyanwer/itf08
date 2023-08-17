products = []
while True:
    selection = int(input("1.Add New Product\n2.Print Product Details"
                          "\n3.Buy Product"
                          "\n4.Delete Product"
                          "\n5.Exit"))
    if selection == 1:
        product_number = input("Enter Product Number :")
        product_name = input("Enter Product Name :")
        product_price = input("Enter Product Price :")
        product_qty = int(input("Enter Product Quantity :"))
        product = {
            "id": product_number,
            "name": product_name,
            "price": product_price,
            "qty": product_qty
        }
        products.append(product)
        print("Product Added Successfully")
    elif selection == 2:
        product_number = input("Enter product number :")
        is_exit= False
        for i in products:
            if i['id'] == product_number:
                print(i)
                is_exit=True
                break
            if not is_exit:
                print("product not exit")

    elif selection == 3:
        # TODO :: input Product Number
        product_number = input("Enter Product Number :")
        # TODO :: input Quantity as integer
        product_qty = int(input("Enter Product Quantity :"))
        # TODO :: update quantity after purchase
        for i in products:
            if i['id'] == product_number:
                while True:
                    product_qty = int(input("Enter Product Quantity :"))
                    if product_qty > i['qty'] or product_qty<=0:
                        print("Invalid qty")
                    else:
                        break
                    i['qty']=i['qty']-product_qty
                    break
    elif selection == 4:
        product_number = input("Enter Product Number :")
        for i in products[:]:
            if i['id'] == product_number:
                products.remove(i)

                break

        # TODO :: input Product Number
        # TODO :: delete Product

    else:
        exit()
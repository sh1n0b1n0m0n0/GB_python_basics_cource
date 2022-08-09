def main():
    products_list = []
    df_prod_names = []
    df_prod_price = []
    df_prod_amount = []
    df_prod_unit = []

    while True:
        product_name = input('Enter product name: ')
        product_price = int(input('Enter the product price: '))
        product_amount = int(input('Enter the product amount: '))
        product_unit = input('Enter the product unit: ')

        product_len = len(products_list)
        product_element = (product_len+1, {"product_name": product_name,
                                           "product_price": product_price,
                                           "product_amount": product_amount,
                                           "product_unit": product_unit})

        products_list.append(product_element)

        ans = input("Do you want enter more products? (y/n)")
        if ans.lower() == 'n':
            break

    print(products_list)

    for elem in products_list:
        df_prod_names.append(elem[1].get("product_name"))
        df_prod_price.append(elem[1].get("product_price"))
        df_prod_amount.append(elem[1].get("product_amount"))
        df_prod_unit.append(elem[1].get("product_unit"))

    df = {"product_name": df_prod_names,
          "product_price": df_prod_price,
          "product_amount": df_prod_amount,
          "product_unit": list(set(df_prod_unit))}

    print(df)


if __name__ == '__main__':
    main()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from django.shortcuts import render
from .models import graphEnquiry
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import seaborn as sns
from shutil import copy2
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
import matplotlib.style as style
style.use('dark_background')


def index(request):
    if request.method == 'POST':
        # handle form submission
        preference = int(request.POST.get('prefrence'))
        # do something with the preference
        return redirect('analysis_form',{'preference': preference})
    else:
        # display preference form
        return render(request, 'prefrence_form.html')


def preference(request):
    if request.method == 'POST':
        preference = request.POST.get('prefrence')
        print(preference)
        if preference == "store_analysis":
            return redirect('store_analysis')
        elif preference == "product_analysis":
            return redirect('product_analysis')
        elif preference == None: 
            return HttpResponse("please go and fuck out of it.enjoy dumbass chatbot")
            
    else: 
            return render(request,'prefrence_form.html')




def chalMeriRani(preference): 
    sales = pd.read_csv('C:/Users/dell/Desktop/Big Mart Sales Prediction/Train-set.csv')
    # matching x_axis and y_axis value with column
    
    sales_data = sales.sort_values(by='EstablishmentYear', ascending=False) # move this line up
    store_names = sales_data['OutletType'].unique()
    for store_name in store_names:
        if preference.lower() in store_name.lower():
            preference = store_name
            break

    
    #  we have store_name, x_quantity and y_quantity
    

    # now we will ask the user upto which row he wants to analyse data.
    fileName = "" 
    # Get the unique store names from the sales data
    store_names = sales_data['OutletType'].unique()
    fig,ax = plt.subplots()
    # Find the store type that matches the user input

    # Get the data for the selected store type
    interest_data = sales_data[sales_data['OutletType'] == preference]

    # Get the unique values in the x_column and sort theminterest_data = sales_data[sales_data['OutletType'] == user_interest]
    # Get the unique values in the x_column and sort them
    store_locations = np.array(interest_data['LocationType'].unique())
    store_sales = []
    store_sales1 = []
    store_sales2 = []
    for item in store_locations:
        location_data = interest_data[interest_data['OutletType'] == preference]
        column_max = location_data['OutletSales'].max()
        store_sales.append(column_max)

    for item in store_locations:
        location_data = interest_data[interest_data['OutletType'] == preference]
        column_min = location_data['OutletSales'].min()
        store_sales1.append(column_min)

    for item in store_locations:
        location_data = interest_data[interest_data['OutletType'] == preference]
        column_mean = location_data['OutletSales'].mean()
        store_sales2.append(column_mean)


    # Set the x-ticks to the x_values
    ax.bar(store_locations, store_sales1, width=0.25, label= 'Face Cream sales data ', align='edge')
    ax.bar(store_locations, store_sales, width=-0.25, label= 'shop store location data', align= 'edge')
    ax.set_xticks(store_locations)
    ax.set_yticks(store_sales)

    # Set the title and legend
    ax.set_title(f'Outlet sales for {preference}')
    ax.legend()
    timestamp = str(int(time.time()))
    file_name = f"static/New folder/plot_{timestamp}.png"
    fig.savefig(file_name)
    # Close the figure
    plt.close(fig)
    # Show the plot
    return file_name; 




def chalMeriRandi(store_name): 
    sales = pd.read_csv('C:/Users/dell/Desktop/Big Mart Sales Prediction/Train-set.csv')
    # matching x_axis and y_axis value with column
    
    sales_data = sales.sort_values(by='EstablishmentYear', ascending=False) # move this line up
    store_names = sales_data['OutletType'].unique()
    print(store_names)
    # Get the data for the selected store type
    # Get the unique values in the x_column and sort them
    store_sales = []
    store_sales1 = []
    fig, ax = plt.subplots(figsize=(8, 6))
    if(store_name == 'bar_chart'):
        # Set the title and legend
        for item in store_names:
            store_data = sales_data[sales_data['OutletType'] == item]
            column_max = store_data['OutletSales'].max()
            store_sales.append(column_max)


        for item in store_names:
            store_data = sales_data[sales_data['OutletType'] == item]
            column_max = store_data['OutletSales'].min()
            store_sales1.append(column_max)



        ax.bar(store_names, store_sales, width=0.25, label='maximum sales of the store', align='edge')
        ax.bar(store_names, store_sales1, width=-0.25, label='minimum sales of the store', align='edge')
        ax.set_xticks(store_names)
        # plt.yticks(store_sales1)
        # Show the plot
        ax.set_title('Comparision of sales made by each stores') 
        ax.legend()
        timestamp = str(int(time.time()))
        file_name = f"static/New folder/plot_{timestamp}.png"
        fig.savefig(file_name)
        # Close the figure
        plt.close(fig)
        # Show the plot
        return file_name;


    elif(store_name == 'pie_chart'):
        marketData = []
        for item in store_names:
            store_data = sales_data[sales_data['OutletType'] == item]
            column_max = store_data['OutletSales'].sum()
            marketData.append(column_max)

        plt.axis('equal')
        plt.pie(marketData,labels=store_names,autopct='%1.1f%%')
        ax.set_title('representation of sales made by each stores') 
        ax.legend()
        timestamp = str(int(time.time()))
        file_name = f"static/New folder/plot_{timestamp}.png"
        fig.savefig(file_name)
        # Close the figure
        plt.close(fig)
        # Show the plot
        return file_name;

    # return HttpResponse("Hello")




def padhaiKarle(store_name,chart_type,mylst):
    sales_data = pd.read_csv('C:/Users/dell/Desktop/Big Mart Sales Prediction/Train-set.csv')

    # filter data for given store_name
    store_data = sales_data[sales_data['OutletType'] == store_name]

    # get unique product types and their sales
    product_types = store_data['ProductType'].unique()
    product_sales = []
    product_max_sales = []
    product_min_sales = []
    
    for product in product_types:
        product_sales.append(store_data[store_data['ProductType'] == product]['OutletSales'].sum())

    for product in product_types:
        product_max_sales.append(store_data[store_data['ProductType'] == product]['OutletSales'].max())

    for product in product_types:
        product_min_sales.append(store_data[store_data['ProductType'] == product]['OutletSales'].max())

    maximum = max(product_max_sales) 
    minimum = min(product_min_sales)
    max_index = product_max_sales.index(max(product_max_sales)) 
    min_index = product_max_sales.index(min(product_max_sales)) 
    
    mylst[0] = f'the maximum sales were of {maximum} of the store {product_types[max_index]}' 
    mylst[1] = f'the minimum sales were of {minimum} of the store {product_types[min_index]}'

    # create bar chart
    if(chart_type == 'bar'):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(product_types, product_sales, label='Total Sales')
        ax.bar(product_types, product_max_sales, label='Max Sales')
        ax.bar(product_types, product_min_sales, label='Min Sales')
        ax.set_xlabel('Product Type')
        ax.set_ylabel('Sales')
        ax.legend()
        ax.set_title(f'Sales at {store_name} by Product Type')
        plt.xticks(rotation=90)
        plt.tight_layout()

        # Save plot and return file name
        timestamp = str(int(time.time()))
        file_name = f"static/New folder/plot_{timestamp}.png"
        fig.savefig(file_name)
        plt.close(fig)
        return file_name
    
    else: 
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.barh(product_types, product_sales, label='Total Sales')
        ax.barh(product_types, product_max_sales, label='Max Sales')
        ax.barh(product_types, product_min_sales, label='Min Sales')
        ax.set_xlabel('Sales')
        ax.set_ylabel('Product Type')
        ax.set_title(f'Sales at {store_name} by Product Type')
        ax.legend()
        plt.tight_layout()

        # save plot and return file name
        timestamp = str(int(time.time()))
        file_name = f"static/New folder/plot_{timestamp}.png"
        fig.savefig(file_name)
        plt.close(fig)  
        return file_name
    

def dikhaDoSabko(x_column, y_column, user_interest):
     sales = pd.read_csv('C:/Users/dell/Desktop/Big Mart Sales Prediction/Train-set.csv')
    # matching x_axis and y_axis value with column
     column_names = sales.columns.tolist()
     x_axis = "" 
     y_axis = ""
     for item in column_names:
        if x_column.lower() in item.lower():
            x_axis = item

     for item in column_names:
        if y_column.lower() in item.lower():
            y_axis = item

     
     store_names = sales['OutletType'].unique()
     for store_name in store_names:
        if user_interest.lower() in store_name.lower():
            user_interest = store_name
            break

     # Find the store type that matches the user input
     interest_data = sales[sales['OutletType'] == user_interest]
     print(interest_data)
    # Get the unique values in the x_column and sort them
     x_values = np.sort(interest_data[x_column].unique())

    # Calculate the mean, max, and min values for each year using list comprehension
     mean_values = [interest_data[interest_data[x_column] == x_value][y_column].mean() for x_value in x_values]
     max_values = [interest_data[interest_data[x_column] == x_value][y_column].max() for x_value in x_values]
     min_values = [interest_data[interest_data[x_column] == x_value][y_column].min() for x_value in x_values]

    # Create the figure and axis objects
     fig, ax = plt.subplots()

    # Plot the data
     ax.plot(x_values, mean_values, label='Mean sales of the store', marker='o', linewidth=2)
     ax.plot(x_values, max_values, label='Maximum sales of the store in each year', marker='o', linewidth=2)
     ax.plot(x_values, min_values, label='Minimum sales of the store in each year', marker='o', linewidth=2)

    # Set the x-ticks to the x_values
     ax.set_xticks(x_values)

    # Set the title and legend
     ax.set_title(f'Outlet sales for {user_interest}')
     ax.legend()

    # Save the plot and return the file name
     timestamp = str(int(time.time()))
     file_name = f"static/New folder/plot_{timestamp}.png"
     fig.savefig(file_name)
     plt.close(fig)
     return file_name




def store_analysis(request, name=None):
    context ={}
    if request.method == 'POST':
        file_name1 = "" 
        file_name2 = "" 
        file_name3 = "" 
        file_name4 = "" 
        
        print("HELLO") 
        store_name = request.POST.get('store_name')
        year = request.POST.get('store_year')
        x_axis = request.POST.get('x_axis')
        y_axis = request.POST.get('y_axis')
        chart_type = request.POST.get('chart_type') 
        bar_type = request.POST.get('bar_type')  
        text_name1 = f'Sales at {store_name} by Product Type' 
        text_name2 = 'Comparision of sales made by each stores'
        text_name3 = f'Outlet sales for {store_name}'
        text_name4 = f'Outlet sales for {store_name}' 
        maxi1 = f'The Sales of  Maximum when:' 
        mini1 = f'The Sales of  Maximum when:' 
        my_list = [maxi1,mini1] 
        
        if chart_type != None and store_name != None: 
            file_name1 = padhaiKarle(store_name,chart_type,my_list)  
            if file_name1 != None: 
                context = {'image_url1': f'/{file_name1}'}
            print(context) 
            
        
        if chart_type != None: 
            time.sleep(1)
            file_name2 = chalMeriRandi(chart_type)  
            if file_name2 != None: 
                context = {'image_url1': f'/{file_name1}','image_url2': f'/{file_name2}'}
            print(context) 
        
        if store_name != None: 
            time.sleep(1)
            file_name3 = chalMeriRani(store_name) 
            if file_name3 != None: 
                context = {'image_url1': f'/{file_name1}','image_url2': f'/{file_name2}','image_url3': f'/{file_name3}'}
            print(context)

        if x_axis != None and y_axis != None and store_name != None: 
            time.sleep(1)
            file_name4 = dikhaDoSabko(x_axis,y_axis,store_name)
            if file_name4 != None: 
                context = {'image_url1': f'/{file_name1}','image_url2': f'/{file_name2}','image_url3': f'/{file_name3}','image_url4': f'/{file_name4}'}
            print(context)

        print(my_list[0]) 
        print(my_list[1])
        context = {'image_url1': f'/{file_name1}','image_url2': f'/{file_name2}','image_url3': f'/{file_name3}','image_url4': f'/{file_name4}','name1':text_name1,'name2':text_name2,'name3':text_name3,'name4':text_name4,'insight1':my_list[0],'insight2':my_list[1]} 
        return render(request,'base.html',context)
        # return HttpResponse("submitted")
    else:
        context = {'name': name}
        return render(request, 'store_analysis.html', context)



def product_analysis(request,name=None): 
    context ={}
    if request.method == 'POST': 
        product_type = request.POST.get('product_type')
        year = request.POST.get('year')
        x_axis = request.POST.get('x_axis')
        y_axis = request.POST.get('y_axis')
        chart_type = request.POST.get('chart_type')
        
        # defining the string variables. 
        file_name1 = "" 
        file_name2 = "" 
        file_name3 = "" 
        file_name4 = ""
        file_name5 = ""
        file_name6 = ""
        text_name1 = "Sales of a product from the Stores" 
        text_name2 = "Product and " +" "+ y_axis+" " + "Relation"
        text_name3 = "Product Visibility Relation" 
        text_name4 = "Product  Sales  Over  Time" 
        text_name5 = "Product pie chart representation" 
        text_name6 = "Product sales bar representation"
        if product_type != None and y_axis != None: 
            print('first condition is triggered')
            file_name1 = saleByRegions(year,product_type)
            print(file_name1)
            if file_name1 != None: 
                context = {'image_url': f'/{file_name1}'}
            print(context)
            # return render(request,'base.html',context)

        if y_axis != None and x_axis != None and chart_type != None: 
            print('second condition is triggered')
            time.sleep(1)
            file_name2 = ProductPriceRelation(x_axis,y_axis,chart_type,product_type)
            print(file_name2)
            context = {'image_url1': f'/{file_name1}','image_url2': f'/{file_name2}'}
            print(context)
            # return render(request,'base.html',context)

        if x_axis != None and product_type != None and y_axis != None and chart_type != None: 
            print('third condition is triggered')
            time.sleep(1)
            file_name3 =  ProductVisibilityRelation(x_axis,y_axis,product_type)
            print(file_name3)
            context = {'image_url1': f'/{file_name1}','image_url2': f'/{file_name2}','image_url3': f'/{file_name3}'}
            print(context)
            # return render(request,'base.html',context)
        

        if x_axis != None and y_axis != None and product_type != None: 
            print('fourth condition is triggered')
            time.sleep(1)
            file_name4 =  ProductSalesOverTime(x_axis,y_axis,product_type)
            print(file_name4)
            print(context)
            context = {'image_url1': f'/{file_name1}','image_url2': f'/{file_name2}','image_url3': f'/{file_name3}','image_url4': f'/{file_name4}'} 
        
        context = {'image_url1': f'/{file_name1}','image_url2': f'/{file_name2}','image_url3': f'/{file_name3}','image_url4': f'/{file_name4}','y_axis':y_axis}
        print(context)

        if x_axis != None and y_axis != None and product_type != None: 
            print("chain saw man") 
            time.sleep(1) 
            file_name5 = PieSaleProduct(x_axis,y_axis,year);
            context = {'image_url1': f'/{file_name1}','image_url2': f'/{file_name2}','image_url3': f'/{file_name3}','image_url4': f'/{file_name4}','image_url5':f'/{file_name5}'} 

        if x_axis != None and y_axis != None and product_type != None: 
            print("I am Johan Liebert") 
            time.sleep(1) 
            file_name6 = BarSaleProduct(x_axis,y_axis,year);
            context = {'image_url1': f'/{file_name1}','image_url2': f'/{file_name2}','image_url3': f'/{file_name3}','image_url4': f'/{file_name4}','image_url5':f'/{file_name5}','image_url6':f'/{file_name6}'} 

        context = {'image_url1': f'/{file_name1}','image_url2': f'/{file_name2}','image_url3': f'/{file_name3}','image_url4': f'/{file_name4}','image_url5':f'/{file_name5}','image_url6':f'/{file_name6}','name1':text_name1,'name2':text_name2,'name3':text_name3,'name4':text_name4,'name5':text_name5,'name6':text_name6} 

        
        return render(request,'base.html',context)
        # return HttpResponse("SUBMITTED")
    else: 
        return render(request,'product_analysis.html')
    


# product analysis: ************************************************************************************************


def saleByRegions(user_year,user_input): 
    sales2 = pd.read_csv('C:/Users/dell/Desktop/Big Mart Sales Prediction/Train-set.csv')
    sales1 = sales2.loc[0:300, sales2.columns.tolist()]    
    print(type(user_year))
    user_year1 = int(user_year)
    sales = sales1[sales1['EstablishmentYear'] == user_year1] 
    print(sales)
    store_names = sales['ProductType'].unique()
    print(store_names)
    # print(sales)
    for item in store_names:
        if user_input.lower() in item.lower():
            user_input = item
    print(user_input)
    user_intrest_data = sales[sales['ProductType'] == user_input] 
    print(sales1)
    location_list = sales1['OutletType'].unique()
    location_max_sale = []
    location_min_sale = []
    location_mean_sale = []
    for item in location_list:
        location_data = user_intrest_data[user_intrest_data['OutletType'] == item]
        column_max = location_data['OutletSales'].max()
        location_max_sale.append(column_max)

    for item in location_list:
        location_data = user_intrest_data[user_intrest_data['OutletType'] == item]
        column_min = location_data['OutletSales'].min()
        location_min_sale.append(column_min)

    for item in location_list:
        location_data = user_intrest_data[user_intrest_data['OutletType'] == item]
        column_mean = location_data['OutletSales'].mean()
        location_mean_sale.append(column_mean)
    fig,ax = plt.subplots()
    ax.bar(location_list, location_max_sale,  label=f'product {user_input} maximum sales from {user_year}')
    ax.bar(location_list, location_min_sale,  label=f'product {user_input} minimum sales from {user_year}')
    # ax.bar(location_list,location_mean_sale,label='')
    ax.set_xticks(location_list)
    # plt.yticks(store_sales)

    # Set the title and legend
    ax.set_title(f'Outlet sales for {user_input}')
    ax.legend()

    timestamp = str(int(time.time()))
    file_name = f"static/New folder/plot_{timestamp}.png"
    fig.savefig(file_name)
    plt.close(fig)  
    return file_name






def ProductPriceRelation(x_axis, y_axis, chart_type, product_type): 
    sales2 = pd.read_csv('C:/Users/dell/Desktop/Big Mart Sales Prediction/Train-set.csv')
    sales1 = sales2.loc[0:300, sales2.columns.tolist()]
    column_names = sales1.columns.tolist()
    df_sorted = sales1.sort_values(by=x_axis, ascending=False)

    for item in column_names: 
        if x_axis in item: 
            x_axis = item 
    
    for item in column_names: 
        if y_axis in item: 
            y_axis = item 
    
    product_names = sales1['ProductType'].unique()
    for item in product_names: 
        if product_type in item: 
            product_type = item

    sales = df_sorted[df_sorted['ProductType'] == product_type] 
    print(sales)
    store_names = sales['ProductType'].unique()
    print(store_names)
    # return HttpResponse("HELLO")
    user_interest_data = df_sorted[df_sorted['ProductType'] == product_type]
    years = user_interest_data[x_axis].unique()
    product_max_mrp = []
    product_min_mrp = []
    product_mean_mrp = []
    for year in years:
        user_useful_data = user_interest_data[user_interest_data[x_axis] == year]
        column_mean = user_useful_data[y_axis].max()
        product_max_mrp.append(column_mean)

    for year in years:
        user_useful_data = user_interest_data[user_interest_data[x_axis] == year]
        column_mean = user_useful_data[y_axis].min()
        product_min_mrp.append(column_mean)

    for year in years:
        user_useful_data = user_interest_data[user_interest_data[x_axis] == year]
        column_mean = user_useful_data[y_axis].mean()
        product_mean_mrp.append(column_mean)

    
    fig,ax = plt.subplots()

    if chart_type == "line":
        print(product_max_mrp)
        print(product_min_mrp)
        print(product_mean_mrp)
        print(years)
        ax.plot(years, product_max_mrp, marker='o')
        ax.plot(years, product_min_mrp, marker='o')
        ax.plot(years, product_mean_mrp, marker='o')

        ax.set_title(f"The line representation of {y_axis} relation with {x_axis} for {product_type}")
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.legend(loc='upper left')

        timestamp = str(int(time.time()))
        file_name = f"static/New folder/plot_{timestamp}.png"
        fig.savefig(file_name)
        plt.close(fig)  
        return file_name

    elif chart_type == "scatter":
        ax.scatter(years, product_max_mrp,label=f"The scatter representation of {y_axis} relation with {x_axis} for {product_type}")
        ax.scatter(years, product_min_mrp,label=f"The scatter representation of {y_axis} relation with {x_axis} for {product_type}")
        ax.scatter(years, product_mean_mrp,label=f"The scatter representation of {y_axis} relation with {x_axis} for {product_type}")

        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.legend(loc='upper left')
        ax.set_title(f"{product_type} Sales Data")
        ax.grid(True, linewidth=1, linestyle="--")
        timestamp = str(int(time.time()))
        file_name = f"static/New folder/plot_{timestamp}.png"
        print('in function ',file_name)
        fig.savefig(file_name)
        plt.close(fig)  
        return file_name
        


def ProductVisibilityRelation(x_quantity,y_quantity,user_input): 
    sales2 = pd.read_csv('C:/Users/dell/Desktop/Big Mart Sales Prediction/Train-set.csv')
    sales1 = sales2.loc[0:300, sales2.columns.tolist()]
    column_names = sales1.columns.tolist()
    for item in column_names: 
        if x_quantity in item: 
            x_quantity = item 
    
    
    product_names = sales1['ProductType'].unique()
    for item in product_names: 
        if user_input in item: 
            user_input = item
    
    fig,ax = plt.subplots()
    product_data = sales1[sales1['ProductType'] == user_input]
    ax.scatter(product_data[x_quantity],product_data['ProductVisibility'],label=f"The scatter representation of {'ProductVisibility'} relation with {x_quantity} for {user_input}")
    ax.set_xlabel(x_quantity)
    ax.set_ylabel('ProductVisibility')
    ax.legend(loc='upper left')
    ax.set_title(f"{user_input} Sales Data")
    ax.grid(True, linewidth=1, linestyle="--")
    timestamp = str(int(time.time()))
    file_name = f"static/New folder/plot_{timestamp}.png"
    print('in function ',file_name)
    fig.savefig(file_name)
    plt.close(fig)  
    return file_name    



def ProductSalesOverTime(x_quantity,y_quantity,user_input): 
    sales2 = pd.read_csv('C:/Users/dell/Desktop/Big Mart Sales Prediction/Train-set.csv')
    sales1 = sales2
    # print(type(user_year))
    # user_year1 = int(user_year)
    column_names = sales1.columns.tolist()
    for item in column_names: 
        if x_quantity in item: 
            x_quantity = item 
    
    for item in column_names: 
        if y_quantity in item: 
            y_quantity = item 
    
    product_names = sales1['ProductType'].unique()
    for item in product_names: 
        if user_input in item: 
            user_input = item
    fig,ax = plt.subplots()
    product_names = sales1['ProductType'].unique()
    matched_product = None

    for product in product_names:
        if user_input.lower() in product.lower():
            matched_product = product
            break

    if matched_product is None:
        print(f"No product matching '{user_input}' was found in the sales data.")
        return []

    product_data = sales1[sales1['ProductType'] == matched_product]
    store_names = product_data[x_quantity].unique()
    store_data = []

    for store in store_names:
        store_sales = product_data[product_data[x_quantity] == store][y_quantity]
        mean_sales = store_sales.mean()
        store_data.append(mean_sales)

    ax.bar(store_names, store_data,label=f'sales of product')
    ax.set_xticks(store_names)
    ax.set_xlabel(x_quantity)
    ax.set_ylabel(y_quantity)
    ax.set_title(f'Sales of {matched_product} by {x_quantity}')
    ax.legend()
    timestamp = str(int(time.time()))
    file_name = f"static/New folder/plot_{timestamp}.png"
    print('in function ',file_name)
    fig.savefig(file_name)
    plt.close(fig)  
    return file_name    
    

    
def PieSaleProduct(x_axis,y_axis,year):
    sales = pd.read_csv('C:/Users/dell/Desktop/Big Mart Sales Prediction/Train-set.csv')
    # matching x_axis and y_axis value with column
    
    sales_data = sales.sort_values(by='EstablishmentYear', ascending=False) # move this line up
    product_names = sales_data['ProductType'].unique()
    print(product_names)
    # Get the data for the selected store type
    # Get the unique values in the x_column and sort them
    
    sales_data1 = sales_data[sales_data['EstablishmentYear'] == int(year)]
    fig, ax = plt.subplots(figsize=(8, 6))

    marketData = []
    for item in product_names:
        store_data = sales_data1[sales_data1['ProductType'] == item]
        column_max = store_data[y_axis].sum()
        marketData.append(column_max)

    plt.axis('equal')
    plt.pie(marketData,labels=product_names,autopct='%1.1f%%')
    ax.set_title(f'representation of sales made by each stores in {year}') 
    # ax.legend()
    timestamp = str(int(time.time()))
    file_name = f"static/New folder/plot_{timestamp}.png"
    fig.savefig(file_name)
    # Close the figure
    plt.close(fig)
    # Show the plot
    return file_name;


    
def BarSaleProduct(x_axis,y_axis,year):
    sales = pd.read_csv('C:/Users/dell/Desktop/Big Mart Sales Prediction/Train-set.csv')
    # matching x_axis and y_axis value with column
    
    sales_data = sales.sort_values(by='EstablishmentYear', ascending=False) # move this line up
    print(sales_data)
    product_names = sales_data['ProductType'].unique()
    print(product_names)
    # Get the data for the selected store type
    # Get the unique values in the x_column and sort them
    
    # sales_data1 = sales_data[sales_data['EstablishmentYear'] == year]
    fig, ax = plt.subplots(figsize=(8, 6))

    sales_data1 = sales_data[sales_data['EstablishmentYear'] == int(year)]
    print(sales_data1)
    marketData = []
    for item in product_names:
        store_data = sales_data1[sales_data1['ProductType'] == item]
        column_max = store_data[y_axis].count()
        marketData.append(column_max)

    print(marketData)
    plt.barh(product_names,marketData,label=f'Bar representation of product sold')
    ax.set_title(f'representation of sales made by each stores in {year}') 
    ax.legend() 
    # ax.set_xlabel(x_axis) 
    # ax.set_ylabel(y_axis)
    # ax.set_xticks(product_names)
    timestamp = str(int(time.time()))
    file_name = f"static/New folder/plot_{timestamp}.png"
    fig.savefig(file_name)
    # Close the figure
    plt.close(fig)
    # Show the plot
    return file_name;


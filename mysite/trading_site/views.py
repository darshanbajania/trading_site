from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from .models import Products, Customers, User_id, Purchase_details, Home_page_images
from django.core.paginator import Paginator
from django.urls import reverse
from urllib.parse import urlencode
from .forms import Update_Customer_Form, Update_Product_Form, Update_Home_images
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import datetime
from django.utils.timezone import utc
import json
from django.http import JsonResponse
# Create your views here.



#home view
def Home_view(request):
    purchased_items=''
    if request.method == "POST":
        
        product_number = request.POST.get('id')
        # getting the url for displaying full proposal
        # print(product_number)
        base_url = reverse('trading_site:Products_view')
        # creating a string of dictionary
        query_string = urlencode({'category': product_number})
        # passing the base_url and query from this page to url
        url = '{}?{}'.format(base_url, query_string)

        # print(proposal_number)
        return redirect(url)
    all_products = Products.objects.order_by('product_id')
    if request.session.has_key('is_logged_in'):
        current_customer =  Customers.objects.filter(user=  request.user).first()
        if current_customer.currently_purchased_products == "":  
            current_customer.currently_purchased_products='{}'
            current_customer.save()
        purchased_items = len(eval(current_customer.currently_purchased_products))
        print(purchased_items)
    corousal_images = Home_page_images.objects.all().first()

    context = {
        'all_products' : all_products,
        'purchased_items' : purchased_items,
        'images' : corousal_images,
    }
    return render(request,'trading_site/base.html',context)

#products home page
def Home_products_view(request):


    return render(request,'trading_site/home_products.html')

# product detail view
def Product_view(request):
    purchased_items=''
    current_product_id = request.GET.get('category')
    print(current_product_id)        
    selected_product = Products.objects.filter(product_id=current_product_id).first()
    print('product',selected_product)
    print(AnonymousUser.is_authenticated)
    if request.method == "POST":
        if request.session.has_key('is_logged_in'):
            quantity = request.POST.get('quantity')
            purchased_product_id = request.POST.get('product_id')

            temp_dictionary = {}
            print(purchased_product_id)
            current_customer =  Customers.objects.filter(user=  request.user).first()
            curr_purcsd_all_products = current_customer.currently_purchased_products
            if curr_purcsd_all_products != "":
                temp_dictionary = eval(curr_purcsd_all_products)
                # temp_dictionary[purchased_product_id] = quantity
                # current_customer.currently_purchased_products = str(temp_dictionary)
                # current_customer.save()
            temp_dictionary[purchased_product_id] = quantity
            print(len(temp_dictionary))
            current_customer.currently_purchased_products = str(temp_dictionary)
            current_customer.save()
            # current_customer.currently_purchased_products = 
            print(current_customer.currently_purchased_products)
        else:
            return redirect('trading_site:login_view')
    if request.session.has_key('is_logged_in'):
        current_customer =  Customers.objects.filter(user=  request.user).first()
        purchased_items = len(eval(current_customer.currently_purchased_products))
    context = {
        'clicked_items' : selected_product,
        'purchased_items' : purchased_items,
    }

    return render(request,'trading_site/product_view.html',context)

def Single_bed_view(request):
    beds = Products.objects.filter(product_type = 'single')
    if request.method == "POST":
        product_number = request.POST.get('id')
        # getting the url for displaying full proposal
        # print(product_number)
        base_url = reverse('trading_site:Products_view')
        # creating a string of dictionary
        query_string = urlencode({'category': product_number})
        # passing the base_url and query from this page to url
        url = '{}?{}'.format(base_url, query_string)

        # print(proposal_number)
        return redirect(url)

    context = {
        'beds': beds,
    }
    return render(request, 'trading_site/selected_products.html', context)

def Double_bed_view(request):
    beds = Products.objects.filter(product_type = 'double')
    if request.method == "POST":
        product_number = request.POST.get('id')
        # getting the url for displaying full proposal
        # print(product_number)
        base_url = reverse('trading_site:Products_view')
        # creating a string of dictionary
        query_string = urlencode({'category': product_number})
        # passing the base_url and query from this page to url
        url = '{}?{}'.format(base_url, query_string)

        # print(proposal_number)
        return redirect(url)

    context = {
        'beds': beds,
    }

    return render(request, 'trading_site/selected_products.html', context)

def King_bed_view(request):
    beds = Products.objects.filter(product_type = 'King')
    if request.method == "POST":
        product_number = request.POST.get('id')
        # getting the url for displaying full proposal
        # print(product_number)
        base_url = reverse('trading_site:Products_view')
        # creating a string of dictionary
        query_string = urlencode({'category': product_number})
        # passing the base_url and query from this page to url
        url = '{}?{}'.format(base_url, query_string)

        # print(proposal_number)
        return redirect(url)

    context = {
        'beds': beds,
    }
    return render(request, 'trading_site/selected_products.html', context)

def Super_bed_view(request):
    beds = Products.objects.filter(product_type = 'Super')
    if request.method == "POST":
        product_number = request.POST.get('id')
        # getting the url for displaying full proposal
        # print(product_number)
        base_url = reverse('trading_site:Products_view')
        # creating a string of dictionary
        query_string = urlencode({'category': product_number})
        # passing the base_url and query from this page to url
        url = '{}?{}'.format(base_url, query_string)

        # print(proposal_number)
        return redirect(url)

    context = {
        'beds': beds,
    }
    return render(request, 'trading_site/selected_products.html', context)

def Orthopedic_mattress_view(request):
    beds = Products.objects.filter(product_type = 'orthopedic')
    if request.method == "POST":
        product_number = request.POST.get('id')
        # getting the url for displaying full proposal
        # print(product_number)
        base_url = reverse('trading_site:Products_view')
        # creating a string of dictionary
        query_string = urlencode({'category': product_number})
        # passing the base_url and query from this page to url
        url = '{}?{}'.format(base_url, query_string)

        # print(proposal_number)
        return redirect(url)

    context = {
        'beds': beds,
    }
    return render(request, 'trading_site/selected_products.html', context)

def a1000_profit_mattress_view(request):
    beds = Products.objects.filter(product_type = '1000 profit')
    if request.method == "POST":
        product_number = request.POST.get('id')
        # getting the url for displaying full proposal
        # print(product_number)
        base_url = reverse('trading_site:Products_view')
        # creating a string of dictionary
        query_string = urlencode({'category': product_number})
        # passing the base_url and query from this page to url
        url = '{}?{}'.format(base_url, query_string)

        # print(proposal_number)
        return redirect(url)

    context = {
        'beds': beds,
    }
    return render(request, 'trading_site/selected_products.html', context)

def a2000_profit_mattress_view(request):
    beds = Products.objects.filter(product_type = '2000 profit')
    if request.method == "POST":
        product_number = request.POST.get('id')
        # getting the url for displaying full proposal
        # print(product_number)
        base_url = reverse('trading_site:Products_view')
        # creating a string of dictionary
        query_string = urlencode({'category': product_number})
        # passing the base_url and query from this page to url
        url = '{}?{}'.format(base_url, query_string)

        # print(proposal_number)
        return redirect(url)

    context = {
        'beds': beds,
    }
    return render(request, 'trading_site/selected_products.html', context)

# about us page
def About_us_view(request):
    purchased_items=''
    if request.session.has_key('is_logged_in'):
        current_customer =  Customers.objects.filter(user=  request.user).first()
        purchased_items = len(eval(current_customer.currently_purchased_products))
    context = {
        'purchased_items' : purchased_items,
    }
    return render(request,'trading_site/about.html',context)

def Games_view(request):
    purchased_items=''
    if request.session.has_key('is_logged_in'):
        current_customer =  Customers.objects.filter(user=  request.user).first()
        purchased_items = len(eval(current_customer.currently_purchased_products))
    context = {
        'purchased_items' : purchased_items,
    }
    return render(request,'trading_site/Lottery.html',context)

@login_required
# viewving cart
def Cart_view(request):
    if request.session.has_key('is_logged_in'):
        customer_a = Customers.objects.filter(user=  request.user).first()
        if customer_a.address == "address":
            return redirect('trading_site:account_view')
        main_dictionary={}
        total_list=0
        no_products = True
        if request.method == "POST":
            #print(remove_item)
            current_customer =  Customers.objects.filter(user=  request.user).first()
            temp_dict=eval(current_customer.currently_purchased_products)
            reduce_quantity = request.POST.get('minus')
            if reduce_quantity != None:
                temp_dict[reduce_quantity]=int(temp_dict[reduce_quantity])-1  
                current_customer.currently_purchased_products=str(temp_dict)
                current_customer.save()     
            increase_quantity = request.POST.get('plus')
            if increase_quantity != None:
                temp_dict[increase_quantity]=int(temp_dict[increase_quantity])+1  
                current_customer.currently_purchased_products=str(temp_dict)
                current_customer.save()       
            remove_item = request.POST.get('remove')
            if remove_item != None:
                temp_dict.pop(remove_item)
                current_customer.currently_purchased_products=str(temp_dict)
                current_customer.save()
            #print(temp_dict) 
        current_customer =  Customers.objects.filter(user=  request.user).first()
        length = len(current_customer.currently_purchased_products)
        product_ids =eval(current_customer.currently_purchased_products)
        for keys in product_ids:
            #print(keys)
            main_list = []
            
            purchased_item_details = Products.objects.filter(product_id = str(keys)).first()
            main_list.append(purchased_item_details.product_image.url)
            main_list.append(purchased_item_details.product_name)
            main_list.append(purchased_item_details.description)
            main_list.append(product_ids[keys])
            main_list.append(int(purchased_item_details.price)*int(product_ids[keys]))
            total_list+=int(purchased_item_details.price)*int(product_ids[keys])
            #print(main_list)
            #print(purchased_item_details)
            main_dictionary[keys]=main_list
        if str(main_dictionary) == '{}':
            no_products = True
        else:
            no_products = False
        print(total_list)
        #print(main_dictionary)
        context = {
            'product_details' : main_dictionary,
            'purchased' : current_customer,
            'total_amount': total_list,
            'no_products' : no_products,
        }
        return render(request,'trading_site/cart.html',context)
    else:
        return redirect('trading_site:home')     


def Login_View(request):
    # if session is there redirect to profile page
    if request.session.has_key('is_logged_in'):
        return redirect('trading_site:home')
        
    if request.method == 'POST':  # authanticate user using login page

        # getting the username of current user
        username = request.POST.get('username')
        # getting the password of current user
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        # authenticating current user
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:  # A backend authenticated the credentials
            login(request, user)  # logging in the current user
            # make the session true after logging in
            request.session['is_logged_in'] = True
            current_user = Customers.objects.filter(user = request.user).first()
            if current_user.customer_id == "no_id":
                user_id = User_id.objects.all().first()
                current_user.customer_id = int(user_id.new_user_id)
                current_user.save()
                user_id.new_user_id = str(int(user_id.new_user_id)+1)
                user_id.save()
            
            if (username == 'admins'):  # if user is admin redirect it to admin_page
                return redirect('trading_site:admin_page')
            else:
                return redirect('trading_site:home')  # else to the user profile

        else:
            # No backend authenticated the credentials
            return render(request, 'registration/login.html')

    return render(request, 'registration/login.html')


# Shows page to register a new user
def register_view(request):
    # if sessions are there redirect to profile page
    if request.session.has_key('is_logged_in'):
        return redirect('trading_site:home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # form for creating new user
        if form.is_valid():  # if valid then create new user and redirect to login page
            form.save()
            return redirect('trading_site:login_view')
    else:  # if form is not correct redirect to the the reggister page with a form
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})    


def Checkout_view(request):
    if request.session.has_key('is_logged_in'):
        total_amount_list=0
        current_customer =  Customers.objects.filter(user=  request.user).first()
        length = len(current_customer.currently_purchased_products)
        product_ids =eval(current_customer.currently_purchased_products)
        for keys in product_ids:
            #print(keys)           
            purchased_item_details = Products.objects.filter(product_id = str(keys)).first()
            total_amount_list+=int(purchased_item_details.price)*int(product_ids[keys])
        context={
            'total_amount_list':total_amount_list,
            'product_id':'complete'
        }
        
        return render(request,'trading_site/checkout.html',context) 
    else:
        return redirect('trading_site:login_view')


def Order_Checkout_view(request):
    if request.session.has_key('is_logged_in'):
        body = json.loads(request.body)
        body_value = body['product_id']
        if body_value == 'complete':
            temp_list = []
            current_customer =  Customers.objects.filter(user=  request.user).first()
            count_temp =Purchase_details.objects.all().count()
            new_purchase = Purchase_details(purchase_id = str(int(count_temp)+1), customers_purchased_id = current_customer.customer_id, time_of_purchase= datetime.datetime.now(), products_detail = current_customer.currently_purchased_products)
            new_purchase.save()
            product_ids =eval(current_customer.currently_purchased_products)
            product_ids_list = list(product_ids.keys())
            for id in product_ids_list:
                product = Products.objects.filter(product_id=str(id)).first()
                product.stock=str(int(product.stock)-int(product_ids[id]))
                print(product.stock)
                product.save()
            current_customer.purchased_product_id='[]'
            now = datetime.datetime.now()
            temp_list.append(current_customer.currently_purchased_products)
            temp_list.append(now)
            temp=eval(current_customer.purchased_product_id)
            temp.append(temp_list)
            current_customer.purchased_product_id = str(temp)
            current_customer.currently_purchased_products = '{}'
            current_customer.save()
            print(current_customer.purchased_product_id)

        print('body',body_value)
        return JsonResponse('payment complete', safe=False)
    else:
        return redirect('trading_site:home')


def Customer_profile_view(request):
    return render(request,'trading_site/customer_profile.html')


def Customer_purchase_details_view(request):
    if request.session.has_key('is_logged_in'):
        main_dictionary={}
        total_list=0
        current_customer =  Customers.objects.filter(user=  request.user).first()
        length = len(current_customer.currently_purchased_products)
        product_ids =eval(current_customer.purchased_product_id)
        print(product_ids)
        if product_ids != []:
            temp_value = eval(product_ids[0][0])
            for keys in temp_value:
                #print(keys)
                main_list = []
                
                purchased_item_details = Products.objects.filter(product_id = str(keys)).first()
                main_list.append(purchased_item_details.product_image.url)
                main_list.append(purchased_item_details.product_name)
                main_list.append(purchased_item_details.description)
                main_list.append(temp_value[keys])
                main_list.append(int(purchased_item_details.price)*int(temp_value[keys]))
                total_list+=int(purchased_item_details.price)*int(temp_value[keys])
                #print(main_list)
                #print(purchased_item_details)
                main_dictionary[keys]=main_list
            
            # print(total_list)
        #print(main_dictionary)
        else:
            main_dictionary = {}
        # now = product_ids[0][1]
        context = {
            'product_details' : main_dictionary,
            'purchased' : current_customer,
            'total_amount': total_list,
            # 'mydate' : now,
        }
        
        # print(now)
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        print(now)
        return render(request,'trading_site/customer_purchase_details.html',context)
    else:
        return redirect('trading_site:home')


def Accounts_view(request):
    if request.session.has_key('is_logged_in'):
        if request.method == 'POST':  # for creating an instance of profile update form with passed details
            p_form = Update_Customer_Form(request.POST,
                                       request.FILES,
                                       instance=request.user.Profile)
            # print(p_form)
            if p_form.is_valid():  # if form is valid then save it
                p_form.save()  # and give a success messsage
                # messages.success(request, f'Your account has been updated')
                return redirect('trading_site:account_view')
        else:  # create an instance of form with current details
            p_form = Update_Customer_Form(instance=request.user.Profile)
            print(p_form)
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('trading_site:account_view')
        else:
            messages.error(request, 'Please correct the error below.')
        current_customer = Customers.objects.filter(user = request.user).first()
        address = current_customer.address
        context = {
            'p_form': p_form,  # passing the form to the update profile page
            'password_change_form': password_form,
            'Address' : address,
        }


        return render(request, 'trading_site/customer_account.html',context)
    else:
        return redirect('trading_site:home')


def Admin_dashboard_view(request):
    if request.session.has_key('is_logged_in'):
        # temp1 = Purchase_details(purchase_id = '', customers_purchased_id = '55449957')
        # temp1.save()
        # temp = Purchase_details.objects.filter(purchase_id = '2').first()
        # print(temp.customers_purchased_id)
        # customer = Customers.objects.filter(customer_id=temp.customers_purchased_id).first()
        # product_information = eval(customer.purchased_product_id)
        # temp.time_of_purchase = product_information[0][1]
        # temp.products_detail = customer.purchased_product_id
        # print(temp.time_of_purchase)
        # temp.save()
        if request.method == 'POST':
            customer_details = request.POST.get('customer_details')
            print(customer_details)
            base_url = reverse('trading_site:admin_customer_details')
            # creating a string of dictionary
            query_string = urlencode({'category': customer_details})
            # passing the base_url and query from this page to url
            url = '{}?{}'.format(base_url, query_string)

            # print(proposal_number)
            return redirect(url)

        temporary_value =[]
        temp2 = Purchase_details.objects.order_by('time_of_purchase')
        print(temp2)
        for purchases in temp2:
            temp = []
            temp.append(purchases.purchase_id)
            temp.append(purchases.customers_purchased_id)
            customer = Customers.objects.filter(customer_id = purchases.customers_purchased_id).first()
            temp.append(customer.full_name)
            temp.append(purchases.time_of_purchase)
            product_information = eval(customer.purchased_product_id)            
            if str(product_information) != '[]':
                product_temp_variable = eval(product_information[0][0])
                # print(len(product_temp_variable))
                product_id = list(product_temp_variable.keys()) 
                # print(product_id)
                product_temporary_var = ""
                for key in product_id:
                    product = Products.objects.filter(product_id=key).first()
                    if product_temporary_var == "":
                        product_temporary_var = product.product_name
                    else:
                        product_temporary_var = product_temporary_var + ", " + product.product_name

                temp.append(product_temporary_var)
            temporary_value.append(temp)

        # print(temp2)
        all_customers = Customers.objects.order_by('customer_id')
        length=all_customers.count()
        all_customer_product_info=[]
        for customer in all_customers:
            customer_product_info=[]
            customer_product_info.append(customer.customer_id)
            customer_product_info.append(customer.full_name)
            product_information = eval(customer.purchased_product_id)
            if str(product_information) != '[]':
                customer_product_info.append(product_information[0][1])
                product_temp_variable = eval(product_information[0][0])
                # print(len(product_temp_variable))
                product_id = list(product_temp_variable.keys()) 
                # print(product_id)
                product_temporary_var = ""
                for key in product_id:
                    product = Products.objects.filter(product_id=key).first()
                    if product_temporary_var == "":
                        product_temporary_var = product.product_name
                    else:
                        product_temporary_var = product_temporary_var + ", " + product.product_name
                customer_product_info.append(product_temporary_var)
                product_temporary_var = ""
                for key in product_id:
                    product = product_temp_variable[key]
                    if product_temporary_var == "":
                        product_temporary_var = str(product)
                    else:
                        product_temporary_var = product_temporary_var + ", " + str(product)
                customer_product_info.append(product_temporary_var)
                # customer_product_info.append(product_temp_variable[product_id[0]])
                # print(product)
            else:
                customer_product_info.append('')
                customer_product_info.append('')

            
            all_customer_product_info.append(customer_product_info)
        # print(all_customer_product_info)
        user_id = User_id.objects.all().first()
        #print(type(int(user_id.new_user_id)))
        context = {
            'customers' : temporary_value,
            'all_customers' : all_customers,
            'all_customer_product_info' : all_customer_product_info
        }
        return render(request,'trading_site/admin_dashboard.html',context)
    else:
        return redirect('trading_site:home')


def Admin_customer_details_view(request):
    if request.session.has_key('is_logged_in'):
        current_customer_id = request.GET.get('category')
        print(current_customer_id)
        main_dictionary={}
        total_list=0
        current_customer =  Customers.objects.filter(customer_id=  current_customer_id).first()
        # length = len(current_customer.currently_purchased_products)
        product_ids =eval(current_customer.purchased_product_id)
        # print(product_ids)
        temp_value = eval(product_ids[0][0])
        for keys in temp_value:
            #print(keys)
            main_list = []
            
            purchased_item_details = Products.objects.filter(product_id = str(keys)).first()
            main_list.append(purchased_item_details.product_image.url)
            main_list.append(purchased_item_details.product_name)
            main_list.append(purchased_item_details.description)
            main_list.append(temp_value[keys])
            main_list.append(int(purchased_item_details.price)*int(temp_value[keys]))
            total_list+=int(purchased_item_details.price)*int(temp_value[keys])
            #print(main_list)
            #print(purchased_item_details)
            main_dictionary[keys]=main_list
        
        print(total_list)
        print(main_dictionary)
        now = product_ids[0][1]
        context = {
            'product_details' : main_dictionary,
            'purchased' : current_customer,
            'total_amount': total_list,
            'mydate' : now,
        }
        
        return render(request, 'trading_site/admin_customer_details.html',context)
    else:
        return redirect('trading_site:home')


def Admin_product_update_view(request):
    if request.session.has_key('is_logged_in'):
        image_object = Home_page_images.objects.all().first()
        temp_object = Products.objects.filter(product_id='1').first()
        p_u_form = Update_Product_Form()
        p_c_form = Update_Product_Form(instance=temp_object)
        h_i_form = Update_Home_images(instance=image_object)
        # print("temp object",temp_object.product_id)
        # print(request.method)
        if request.method == 'POST':  # for creating an instance of profile update form with passed details
            form_product_id = request.POST.get('product')
            print('form_product_id',form_product_id)


            # temp_object = Products.objects.filter(product_id=form_product_id).first()
            print('hello world')
            full_form_value=request.POST.get('full_form')
            blank_form_value=request.POST.get('blank_form')
            image_form_value = request.POST.get('image_form')
            print('hello',blank_form_value)
            
            if blank_form_value=="1":
                p_u_form = Update_Product_Form(request.POST,
                                        request.FILES)

                print(p_u_form.is_valid())
                if p_u_form.is_valid():  # if form is valid then save it
                    p_u_form.save()  # and give a success messsage
                temp = Products.objects.filter(product_id='').first()
                temp.product_id = str(Products.objects.count())
                temp.save()
                print(temp.product_name)

                return redirect('trading_site:product_update')
            p_c_form =Update_Product_Form(instance=temp_object)
            # if full_form_value=='2':    
            #     p_c_form = Update_Product_Form(request.POST,
            #                             request.FILES,
            #                             instance=temp_object)
            
            #     if p_c_form.is_valid():  # if form is valid then save it
            #         p_c_form.save()  # and give a success messsage
            #     # print(p_u_fo)rm
            # # if p_u_form.is_valid():  # if form is valid then save it
            # #     p_u_form.save()  # and give a success messsage
            #     # messages.success(request, f'Your account has been updated')
            #     return redirect('trading_site:product_update')
            if image_form_value=="3":
                h_i_form = Update_Home_images(request.POST,
                                        request.FILES,
                                        instance=image_object)

                if h_i_form.is_valid():  # if form is valid then save it
                    h_i_form.save()  # and give a success messsage
                return redirect('trading_site:product_update')
            if form_product_id == None:
                form_product_id='1'
            if int(form_product_id) >0 and int(form_product_id)<=Products.objects.all().count():
                print(form_product_id)
                # getting the url for displaying full proposal
                # print(product_number)
                base_url = reverse('trading_site:admin_product_detail_update')
                # creating a string of dictionary
                query_string = urlencode({'category': form_product_id})
                # passing the base_url and query from this page to url
                url = '{}?{}'.format(base_url, query_string)

                # print(proposal_number)
                return redirect(url)
        else:  # create an instance of form with current details
            # temp_object = Products.objects.filter(product_id='1').first()
            p_u_form = Update_Product_Form()
            # p_c_form = Update_Product_Form(instance=temp_object)
            h_i_form = Update_Home_images(instance=image_object)
        all_products = Products.objects.order_by('product_id')
        print("temp object 2",temp_object)
        context = {
            'p_u_form':p_u_form,
            # 'p_c_form': p_c_form,
            'h_i_form' : h_i_form,
            'product_preview': temp_object,
            'all_products' : all_products,
        }     
        return render(request,'trading_site/admin_product_update.html',context)
    else:
        return redirect('trading_site:home')

def Admin_products_detail_update_view(request):
    if request.session.has_key('is_logged_in'):
        product_detail_id = request.GET.get('category')
        if request.method == 'POST':  
            full_form_value=request.POST.get('full_form')
            temp_object = Products.objects.filter(product_id=product_detail_id).first()
            if full_form_value=='2':    
                p_c_form = Update_Product_Form(request.POST,
                                        request.FILES,
                                        instance=temp_object)
            
                if p_c_form.is_valid():  # if form is valid then save it
                    p_c_form.save()  # and give a success messsage
                return redirect('trading_site:product_update')
        else:
            temp_object = Products.objects.filter(product_id=product_detail_id).first()
            p_c_form = Update_Product_Form(instance=temp_object)
        context = {
            'p_c_form' : p_c_form,
            'product_preview': temp_object,
        }
        return render(request, 'trading_site/admin_products_detail_update.html',context)
    else:
        return redirect('trading_site:home')


    

from flask import Flask, render_template, request
import json
app = Flask(__name__)


# Istantiate Databse
#Idealluse MongoDb or SQL
with open("database.json") as f:
    database = json.loads(f.read())
    copy_db = database.copy()
 

@app.route("/", methods=['POST','GET'])
def index():

    if request.method == 'POST':

        data = request.form

        
        flavor1, flavor2, flavor3, flavor4 = data["perfume1"], data["perfume2"], data["perfume3"], data["perfume4"]

        ordered_scoops = [flavor1, flavor2, flavor3, flavor4]
        ordered_scoops_dct ={}


        # We iterate through the ordered_scoops list to create the ordered_scoops_dct
        # The dictionary count the number of time a flavor was present in the list
        
        for i in ordered_scoops:
            if i in ordered_scoops_dct.keys():
                ordered_scoops_dct[i] +=1
            else:
                ordered_scoops_dct[i] = 1
        print(ordered_scoops_dct)
        
        #We create a total price list to add all the prices is the flavor is available
        total_price = []

        # We iterate through the ordered_scoops_dct to find it's information in the database
        for flavor, count in ordered_scoops_dct.items():
            if  count > database[flavor]['stock']: 
                return render_template("website.html", availability = "Out of Stock")
            else:
                total_price.append(database[flavor]['price']*count)
        
        return render_template("website.html", total_amount = sum(total_price), availability = "In Stock")
    
    return render_template("website.html")


if __name__ == "__main__":
    app.run(debug=True)
















# #1111111111111111111111111111111111111111111111111111111

# from flask import Flask, render_template, request
# import json
# app = Flask(__name__)

# with open("database.json") as f:
#     database = json.loads(f.read())


# @app.route("/", methods = ['POST', 'GET'])
# def index():

#     if request.method == 'POST':

#         data = request.form


#         flavor1, flavor2, flavor3, flavor4 = data["perfume1"], data["perfume2"], data["perfume3"], data["perfume4"]











# #22222222222222222222222222222222222222222222222222222222222222


#         ordered_scoops = [flavor1, flavor2, flavor3, flavor4]
#         ordered_scoops_dct = {}

#         for i in ordered_scoops: 
#             if i in ordered_scoops_dct.keys():
#                 ordered_scoops_dct[i] += 1
#             else: 
#                 ordered_scoops_dct[i] = 1
#             print(ordered_scoops_dct)




















# #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333
 
            
#             total_price = []

#             for flavor, count in ordered_scoops_dct.items():
#                 if count > database[flavor]['stock']:
#                     return render_template("website.html", availability = "Out of Stock")
                
#                 else: 
#                     total_price.append(database[flavor]['price']*count)

#             return render_template("webite.html", total_amount = sum(total_price), availability = "In Stock")
#         return render_template("website.html")





# if __name__ == "__main__":     
#     app.run(debug=True)













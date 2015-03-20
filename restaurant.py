'''
Given
{
    #"Restaurant Types"."[categoryNames]"
    "American" : "[Burger, French fries, Potato Chips]",
    "Italian":"[Pizza,Bread Sticks, Potato Chips]"
}
Assume this kind of data is given as input and loaded into your choice of Data Structure.
Using Category name return the no of resturarnt type. Ex: if i/p is Potato Chips, O/P should be : 2 (American and Italian).
Please mention your Data structure and logic.

***Hash table/dictionary -> access run time is O(1)***
'''
def load_data(restaurants):
    if isinstance(restaurants, dict):
        foods = {}
        for key, value in restaurants.iteritems():
            for food in value:
                if food in foods:
                    foods[food].append(key)
                else:
                    foods[food] = [key]
        return foods

#Test case

restaurants = {
"American": ["Burger", "French fries", "Potato Chips"],
"Italian": ["Pizza", "Bread Sticks", "Potato Chips"],
}
print load_data(restaurants)

# patterns

## several patterns (creational)

The code that uses the factory method (often called the client code) doesn’t see a difference between the actual products returned by various subclasses. The client treats all the products as abstract Transport. The client knows that all transport objects are supposed to have the deliver method, but exactly how it works isn’t important to the client.


**Problem**


Imagine that you’re creating a logistics management application. The first version of your app can only handle transportation by trucks, so the bulk of your code lives inside the ``Truck`` class.

After a while, your app becomes pretty popular. Each day you receive dozens of requests from sea transportation companies to incorporate sea logistics into the app.


![image1](https://refactoring.guru/images/patterns/diagrams/factory-method/problem1-en.png?id=de638561be0bbb1025ada6bfcb815def)


Great news, right? But how about the code? At present, most of your code is coupled to the Truck class. Adding Ships into the app would require making changes to the entire codebase. Moreover, if later you decide to add another type of transportation to the app, you will probably need to make all of these changes again.

As a result, you will end up with pretty nasty code, riddled with conditionals that switch the app’s behavior depending on the class of transportation objects.


**Solution**

The Factory Method pattern suggests that you replace direct object construction calls (using the ``new`` operator) with calls to a special factory method. Don’t worry: the objects are still created via the ``new`` operator, but it’s being called from within the factory method. Objects returned by a factory method are often referred to as products.

![image2](https://refactoring.guru/images/patterns/diagrams/factory-method/solution1.png?id=fc756d2af296b5b4d482e548214d08ef)

At first glance, this change may look pointless: we just moved the constructor call from one part of the program to another. However, consider this: now you can override the factory method in a subclass and change the class of products being created by the method.

There’s a slight limitation though: subclasses may return different types of products only if these products have a common base class or interface. Also, the factory method in the base class should have its return type declared as this interface.

![image3](https://refactoring.guru/images/patterns/diagrams/factory-method/solution2-en.png?id=db5de848c1d490b835666ef54d131d46)

For example, both ``Truck`` and ``Ship`` classes should implement the Transport interface, which declares a method called ``deliver``. Each class implements this method differently: trucks deliver cargo by land, ships deliver cargo by sea. The factory method in the ``RoadLogistics`` class returns truck objects, whereas the factory method in the ``SeaLogistics`` class returns ships.

![image4](https://refactoring.guru/images/patterns/diagrams/factory-method/solution3-en.png?id=b6f53911fc0d56f9ef99501fc4aec059)

The code that uses the factory method (often called the __client__ code) doesn’t see a difference between the actual products returned by various subclasses. The client treats all the products as abstract ``Transport``. The client knows that all transport objects are supposed to have the ``deliver`` method, but exactly how it works isn’t important to the client.

## several patterns (structural)

Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.


**Problem**


Imagine that you’re creating a stock market monitoring app. The app downloads the stock data from multiple sources in XML format and then displays nice-looking charts and diagrams for the user.

At some point, you decide to improve the app by integrating a smart 3rd-party analytics library. But there’s a catch: the analytics library only works with data in JSON format.

![image5](https://refactoring.guru/images/patterns/diagrams/adapter/problem-en.png?id=60d01f6c72ba85030cd52d5955caa3d8)

You could change the library to work with XML. However, this might break some existing code that relies on the library. And worse, you might not have access to the library’s source code in the first place, making this approach impossible.


**Solution**


You can create an ``adapter.`` This is a special object that converts the interface of one object so that another object can understand it.

An adapter wraps one of the objects to hide the complexity of conversion happening behind the scenes. The wrapped object isn’t even aware of the adapter. For example, you can wrap an object that operates in meters and kilometers with an adapter that converts all of the data to imperial units such as feet and miles.

Adapters can not only convert data into various formats but can also help objects with different interfaces collaborate. Here’s how it works:

1. The adapter gets an interface, compatible with one of the existing objects.
2. Using this interface, the existing object can safely call the adapter’s methods.
3. Upon receiving a call, the adapter passes the request to the second object, but in a format and order that the second object expects.

Sometimes it’s even possible to create a two-way adapter that can convert the calls in both directions.
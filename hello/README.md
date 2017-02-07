# Hello
The world's most convoluted Hello World program.  It uses a giant stack to
echo your hello through an api endpoint.

 + Send: a GET request to api.storn.co/v1/api/hello/echo?hello=hello-world
 
 + Receive: An echo of the hello parameter value and a count of the
 number of times that the parameter has been echoed.
 
 + Django Rest Framework > Django > Python > PostgreSQL on AWS

Check out the public API at: http://api.stornco.com

## Some interesting code:

> Check out the custom *HelloSerializer*, which removes the unique validation
for Hello.word.  It's a handy approach for hacking the out-of-the
 box DRF validation.
 
https://github.com/StornWhite/stornco-api/blob/master/hello/serializers.py#L11-L21
 
 
> Check out *HelloAPITestCase* which runs a bunch of canned, situation-
based tests via Mixins to the BaseAPITestCase class.

https://github.com/StornWhite/stornco-api/blob/master/hello/tests/api/test_hello.py#L10-L16
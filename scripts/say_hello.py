# -*- coding: utf-8 -*-

def hello_world():
    return 'Hello World'

def hello_universe():
    return 'Hello Universe'

def hello(name):
    return 'Hello {}'.format(name)

def main():
    print(hello_universe())
    print(hello('MT student'))
	print(hello_world())

if __name__ == '__main__':
    main()

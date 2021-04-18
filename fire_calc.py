# https://youtu.be/JqyqWv3MUBM
import fire

class SimpleCalc(object):
    def double(self,number):
        return 2 * number

if __name__ == '__main__':
    fire.Fire(SimpleCalc)


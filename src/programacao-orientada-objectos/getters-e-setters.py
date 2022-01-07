class ImprimePassowrd:
    def __init__(self, name:str, password:int) -> None:
        self.name = name;
        self.__password = password;


    def get_password(self) -> int:
        return self.__password;

    def set_password(self, newPassword:int) -> None:
        self.__password = newPassword;

impreme = ImprimePassowrd('yazalde', 1234);


print(impreme.get_password());

impreme.set_password(98765);

print(impreme.get_password());


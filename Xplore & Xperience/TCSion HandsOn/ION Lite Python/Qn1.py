class Account():
    def __init__(self,accntNo,accntName,accntBalance):
        self.accntNo=accntNo
        self.accntName=accntName
        self.accntBalance=accntBalance
class AccountDemo():
    def __init__(self):
        pass
    def depositAmnt(self,acnt,depamount):
        self.acnt=acnt
        self.depamount=depamount
        acnt.accntBalance+=depamount
        return acnt.accntBalance
    def withdrawAmnt(self,acnt,withamount):
        self.withamount=withamount
        if acnt.accntBalance-withamount>1000:
            acnt.accntBalance-=withamount
            return acnt.accntBalance
        else:
            return "No Adequate balance"

if __name__ == '__main__':
    accntNo=int(input())
    accntName=input()
    accntBalance=int(input())
    depamount=int(input())
    withamount=int(input())
    acnt=Account(accntNo,accntName,accntBalance)
    acntdemoobj=AccountDemo()
    print(acntdemoobj.depositAmnt(acnt,depamount))
    print(acntdemoobj.withdrawAmnt(acnt,withamount))

public class IciciBankAdapter implements BankApis {

    private IciciBankApi icic;

    public IciciBankAdapter() {
        this.icic = new IciciBankApi();
    }

    @Override
    public void makeTransaction(String accountNo, int amount) {
        this.icic.sendMoney(accountNo, amount);
    }

    @Override
    public int checkBalance(String accountNo) {
        return this.icic.fetchBalance(accountNo);
    }
}
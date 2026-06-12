from account import Account
import pytest

@pytest.fixture
def basic_account():
    return Account('Bob', 100)

@pytest.fixture
def account_with_transaction():
    acc = Account('Bob', 100)
    acc.add_transaction(20)
    acc.add_transaction(-10)
    acc.add_transaction(50)
    return acc

def test_account_structure(basic_account):
    assert basic_account.owner == 'Bob'
    assert basic_account.amount == 100

def test_add_transaction(account_with_transaction):
    assert account_with_transaction._transactions == [20, -10, 50]

def test_balance(account_with_transaction):
    assert account_with_transaction.balance == 160

def test_getitem(account_with_transaction):
    assert account_with_transaction[1] == -10

def test_transaction_len(account_with_transaction):
    assert len(account_with_transaction) == 3

def test_new_account_no_transaction(basic_account):
    assert len(basic_account) == 0

def test_only_owner_is_passed():
    acc = Account('Ales')
    assert acc.balance == 0

def test_repr(account_with_transaction):
    assert repr(account_with_transaction) == 'Account({!r}, {!r})'.format(account_with_transaction.owner, account_with_transaction.amount)

def test_str(account_with_transaction):
    assert str(account_with_transaction) == 'Account of {} with starting amount: {}'.format(account_with_transaction.owner, account_with_transaction.amount)


def test_add_transaction_rejects_non_int(basic_account):
    with pytest.raises(ValueError):
        basic_account.add_transaction(10.5)


def test_account_comparison_operators():
    low = Account('Low', 100)
    low.add_transaction(10)
    high = Account('High', 100)
    high.add_transaction(20)

    assert low < high
    assert high > low

    same_balance = Account('Same', 90)
    same_balance.add_transaction(20)
    assert low == same_balance


def test_account_add_combines_metadata_and_transactions(account_with_transaction):
    other = Account('Alice', 50)
    other.add_transaction(5)

    combined = account_with_transaction + other

    assert combined.owner == 'Bob&Alice'
    assert combined.amount == 150
    assert list(combined) == [20, -10, 50, 5]
import sys
from barista.customer import Customer
import numpy as np


class TestCustomer(Customer):
    def __init__(self, filename):
        compute_semaphore, model_semaphore, handles = \
            Customer.parse_ipc_interface_file(filename)
        Customer.__init__(self, compute_semaphore, model_semaphore, handles)
        self.data = self.arrays['data']
        self.label = self.arrays['label']
        self.conv1_dW = self.arrays['conv1_dW']

    def update_data(self):
        self.data[...] = np.random.randn(*self.data.shape)
        self.label[:] = np.random.choice(xrange(10), size=self.label.shape)
        print "Update data"

    def process_model(self):
        print "Pull out gradients"
        print "Conv1_dW RMS value:", np.linalg.norm(self.conv1_dW)


def main(filename):
    customer = TestCustomer(filename)
    for _ in range(10):
        customer.run_transaction()

if __name__ == "__main__":
    main(sys.argv[1])

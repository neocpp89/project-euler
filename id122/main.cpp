#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <algorithm>

enum class ChainOperation {
    InputInput_StoreInput,
    InputInput_StoreOutput,
    InputOutput_StoreInput,
    InputOutput_StoreOutput,
    OutputOutput_StoreInput,
    OutputOutput_StoreOutput
};

std::ostream &operator<<(std::ostream &os, ChainOperation op)
{
    switch (op) {
        case ChainOperation::InputInput_StoreInput:
            os << "x = x.x";
        break;
        case ChainOperation::InputInput_StoreOutput:
            os << "Y = x.x";
        break;
        case ChainOperation::InputOutput_StoreInput:
            os << "x = x.Y";
        break;
        case ChainOperation::InputOutput_StoreOutput:
            os << "Y = x.Y";
        break;
        case ChainOperation::OutputOutput_StoreInput:
            os << "x = Y.Y";
        break;
        case ChainOperation::OutputOutput_StoreOutput:
            os << "Y = Y.Y";
        break;
    }
    return os;
}

class Chain
{
    private:
        int input_;
        int output_;
        std::vector<ChainOperation> operations_;

        inline void advance(int new_input, int new_output)
        {
            input_ = new_input;
            output_ = new_output;
            return;
        }

    public:
        Chain()
        {
            input_ = 1;
            output_ = 1;
        }

        int getCurrentOutput() const
        {
            return output_;
        }

        int getCurrentInput() const
        {
            return input_;
        }

        void advance(ChainOperation op)
        {
            operations_.push_back(op);
            const int in = input_;
            const int out = output_;
            switch(op)
            {
                case ChainOperation::InputInput_StoreInput:
                    advance(2 * in, out);
                break;
                case ChainOperation::InputInput_StoreOutput:
                    advance(in, 2 * in);
                break;
                case ChainOperation::InputOutput_StoreInput:
                    advance(in + out, out);
                break;
                case ChainOperation::InputOutput_StoreOutput:
                    advance(in, in + out);
                break;
                case ChainOperation::OutputOutput_StoreInput:
                    advance(2 * out, out);
                break;
                case ChainOperation::OutputOutput_StoreOutput:
                    advance(in, 2 * out);
                break;
            }
        }

        size_t getChainLength() const
        {
            return operations_.size();
        }

        std::vector<ChainOperation> getOperations() const
        {
            return operations_;
        }
};

int main(int argc, char **argv)
{
    if (argc != 2) {
        std::cout << argv[0] << ": wanted-exponent\n";
        return 0;
    }
    int want_exponent = std::stoi(std::string(argv[1]));

    std::stack<Chain> queue;
    queue.push(Chain());


    int binary_exponentiation_count = -1;
    int log2w = -1;
    std::string s;
    for (int j = want_exponent; j != 0; j >>= 1) {
        s += std::to_string(j & 1);
        binary_exponentiation_count += (j & 1);
        binary_exponentiation_count++;
        log2w++;
    }
    binary_exponentiation_count--;
    std::reverse(s.begin(), s.end());
    std::cout << "Exponent: " << want_exponent << " " << s << "b\n";

    int best = binary_exponentiation_count;
    while (!queue.empty()) {
        // Chain top = queue.front();
        Chain top = queue.top();
        queue.pop();

        // std::cout << top.getCurrentOutput() << " " << top.getChainLength() << "\n";

        if (top.getChainLength() <= static_cast<std::size_t>(best)) {
            if (top.getCurrentOutput() == want_exponent) {
                std::vector<ChainOperation> v = top.getOperations();
                best = top.getChainLength();
                for (auto op : v) {
                    std::cout << op << "  ";
                }
                std::cout << "    x = x**" << std::setw(4) << std::left << top.getCurrentInput() << " Y = x**" << top.getCurrentOutput() << "\n";
            } else {
                const int in = top.getCurrentInput();
                const int out = top.getCurrentOutput();
                const int max = (in > out)?(in):(out);

                if (max >= want_exponent) {
                    continue;
                }

                // how many squarings would it take
                int log2m = -1;
                {
                    unsigned int b = max;
                    while (b >>= 1) {
                        log2m++;
                    }
                }
                const int steps = (log2w - log2m);
                const int totalSteps = top.getChainLength() + steps - 1;
                if (totalSteps <= best) {
                    Chain ii_i = Chain(top);
                    ii_i.advance(ChainOperation::InputInput_StoreInput);
                    Chain ii_o = Chain(top);
                    ii_o.advance(ChainOperation::InputInput_StoreOutput);
                    Chain io_i = Chain(top);
                    io_i.advance(ChainOperation::InputOutput_StoreInput);
                    Chain io_o = Chain(top);
                    io_o.advance(ChainOperation::InputOutput_StoreOutput);
                    Chain oo_i = Chain(top);
                    oo_i.advance(ChainOperation::OutputOutput_StoreInput);
                    Chain oo_o = Chain(top);
                    oo_o.advance(ChainOperation::OutputOutput_StoreOutput);
                    if (ii_i.getCurrentInput() != in || ii_i.getCurrentOutput() != out) {
                        queue.push(ii_i);
                    }
                    if (io_i.getCurrentInput() != in || io_i.getCurrentOutput() != out) {
                        queue.push(io_i);
                    }
                    if (oo_i.getCurrentInput() != in || oo_i.getCurrentOutput() != out) {
                        queue.push(oo_i);
                    }
                    if (ii_o.getCurrentInput() != in || ii_o.getCurrentOutput() != out) {
                        queue.push(ii_o);
                    }
                    if (io_o.getCurrentInput() != in || io_o.getCurrentOutput() != out) {
                        queue.push(io_o);
                    }
                    if (oo_o.getCurrentInput() != in || oo_o.getCurrentOutput() != out) {
                        queue.push(oo_o);
                    }
                }
            }
        }
    }

    std::cout << "Best length is " << best << ", binary exponentiation is " << binary_exponentiation_count << " for exponent " << want_exponent << ".\n";
    std::cout << best << '\n';

    return 0;
}

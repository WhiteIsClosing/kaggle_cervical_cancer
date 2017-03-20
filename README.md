# kaggle cervical cancer competition

## Project setup

80% training, 20% validation
<pre><code>
git clone https://github.com/YuelongGuo/kaggle_cervical_cancer.git
cd kaggle_cervical_cancer/setup
./setup.sh
</code></pre>

Assuming your downloaded data is in direcotry: "./download/"

## Benchmark 0 - VGG model with training and testing only
In directory "benchmark_0_lecture1_vgg"

fast.ai lecture 1 VGG model, 5 epoches

score 0.97463

## Benchmark 1 - VGG model with additional images
In directory "benchmark_1_lecture1_additional"

fast.ai lecture 1 VGG model

Additional images trained with 5 epoches, train images trained with 1 epoches.

score 0.88499

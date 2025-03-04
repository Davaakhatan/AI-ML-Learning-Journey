# Bayes' Theorem Calculator
def bayes(prior_A, prob_B_given_A, prob_B):
    return (prior_A * prob_B_given_A) / prob_B

# Example: Cancer Test
# P(Cancer) = 0.01, P(Positive Test | Cancer) = 0.9, P(Positive Test) = 0.1
posterior = bayes(0.01, 0.9, 0.1)
print(f"Probability of having cancer given a positive test: {posterior:.2%}")

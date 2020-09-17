function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%
hx = X*theta;
herror = hx -y;
sumSquareError = sum(herror.^2);
FirstTerm = (1/(2*m))*sumSquareError;

thetaSinBias = theta(2:end); % Eliminamos el termino 0 (theta(1))
sumSquareTheta = sum(thetaSinBias.^2);
SecondTerm = (lambda/(2*m))*sumSquareTheta;

J = FirstTerm + SecondTerm;

%%Gradiente
grad = (1/m) * X' * herror;
grad(2:end) += (lambda / m) * thetaSinBias;












% =========================================================================

grad = grad(:);

end

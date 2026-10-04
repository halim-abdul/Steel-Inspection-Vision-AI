function R = weibull_reliability(t,shape,scale)
% Reference reliability curve for comparison with Python implementation.
t = max(t,0);
R = exp(-((t./scale).^shape));
end


p_start = 5;
p_end = 1000;
for p=p_start:p_end
	a = 1:(p-2); 
	b = (2 * p * a - p .* p) ./ (2 * (a - p));
	b = b(b > 0);
	count(p) = sum(1 - (ceil(b) - floor(b))) / 2;
end

find(count == max(count))

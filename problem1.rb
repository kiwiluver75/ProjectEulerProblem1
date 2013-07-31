$sum = 0

for i in 1..999
  if i % 3 == 0 or  i % 5 == 0 then $sum += i end
end

puts($sum)

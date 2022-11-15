#!/usr/bin/env ruby

class Solution
  def self.count
    new.send(:count).result
  end

  def self.by_window
    new.send(:by_window).result
  end

  attr_reader :result

  private

  def initialize
    @result = 0
  end

  def count
    input.count.times do |i|
      @result += 1 if (input[i] - input[i - 1]).positive?
    end
    self
  end

  def by_window
    (input.count - 3).times do |i|
      @result += 1 if (window(i + 1) - window(i)).positive?
    end
    self
  end

  def window(index)
    [input[index], input[index + 1], input[index + 2]].sum
  end

  def input
    @input ||= CSV.read('input.csv').flatten.map(&:to_i)
  end
end

puts "part A: #{Solution.count}"
puts "part B: #{Solution.by_window}"

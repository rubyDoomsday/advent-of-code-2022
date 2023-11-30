#!/usr/bin/env ruby

class Solution
  UP = 'up'.freeze
  DOWN = 'down'.freeze
  FORWARD = 'forward'.freeze

  def self.part_a
    new.send(:dive_a).result.first(2).inject(:*)
  end

  def self.part_b
    new.send(:dive_b).result.first(2).inject(:*)
  end

  attr_reader :result

  private

  def initialize
    # [forward, depth, aim]
    @result = [0, 0, 0]
  end

  def dive_a
    input.each do |axis, number|
      case axis
      when FORWARD then result[0] += number
      when DOWN    then @result[1] += number
      when UP      then @result[1] -= number
      end
    end
    self
  end

  def dive_b
    input.each do |axis, number|
      case axis
      when DOWN then @result[2] += number
      when UP then @result[2] -= number
      else # FORWARD
        result[1] += (number * @result[2])
        @result[0] += number
      end
    end
    self
  end

  def input
    @input ||= CSV.read('input.csv').flatten.map do |line|
      values = line.split(' ')
      [values[0], values[1].to_i]
    end
  end
end

puts "part A: #{Solution.part_a}"
puts "part B: #{Solution.part_b}"

#!/usr/bin/env ruby

class Solution
  def self.test
    new(sample).run
  end

  def self.answer
    new(input).run
  end

  def self.input
    @input ||= File.readlines('input')
  end

  def self.sample
    %w(
      two1nine
      eightwothree
      abcone2threexyz
      xtwone3four
      4nineeightseven2
      zoneight234
      7pqrstsixteen
    )
  end

  attr_reader :result

  def initialize(input)
    @result = build(input)
  end

  def run
    # puts "sample: #{result}"
    puts "sum: #{result.sum}"
  end

  private

  def build(input)
    input.map do |line|
      "#{first(from_left(line))}#{first(from_right(line))}".to_i
    end
  end

  def from_left(line)
    line.gsub(/\d|#{dictionary.keys.join('|')}/) do |matched|
      parse(matched)
    end
  end

  def from_right(line)
    line.reverse.gsub(/\d|#{dictionary.keys.map(&:reverse).join('|')}/) do |matched|
      parse(matched.reverse)
    end
  end

  def first(string)
    string.gsub(/\D/, "")[0]
  end

  def parse(string)
    begin
      Integer(string)
      string
    rescue ArgumentError
      dictionary[string].to_i
    end
  end

  def dictionary
    {
      "eight" => 8,
      "one" => 1,
      "two" => 2,
      "three" => 3,
      "four" => 4,
      "five" => 5,
      "six" => 6,
      "seven" => 7,
      "nine" => 9,
      "zero" => 0,
    }
  end
end

Solution.test
Solution.answer

require 'csv'

input_path = "htmlproofer-output.txt"
output_path = "htmlproofer-report.csv"

rows = []
lines = File.readlines(input_path)
i = 0

while i < lines.size
  line = lines[i]
  
  if line =~ /^\* At (.+?):(\d+):/
    file = $1.strip
    lineno = $2.strip

    # Skip blank lines and fetch next non-empty message
    message = nil
    j = i + 1
    while j < lines.size
      candidate = lines[j].strip
      if !candidate.empty?
        message = candidate
        break
      end
      j += 1
    end

    rows << [file, lineno, message] if message
    i = j
  else
    i += 1
  end
end

CSV.open(output_path, "w") do |csv|
  csv << ["File", "Line", "Message"]
  rows.each { |row| csv << row }
end

puts "✅ Parsed #{rows.size} errors to #{output_path}"
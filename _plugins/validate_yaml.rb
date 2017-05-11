module MyModule

  class WarningGenerator < Jekyll::Generator
    def generate(site)

      total_errors = Array.new

      red = "\e[31m"
      clear = "\e[0m"

      lessons = site.pages.keep_if{|i| i.data["layout"] == "default"}

      lessons.each do |p|

        page_errors = Array.new

        required_fields = ["editors", "reviewers", "authors", "date", "title"]

        required_fields.each do |f|
          if p.data[f].nil?
            page_errors.push("'#{f}' is missing.")
          end
        end

        unit_errors = page_errors.map{|e| "\t - #{e}"}

        unless page_errors.empty?
          warn "#{red}In #{p.dir}#{p.name}:#{clear}"
          unit_errors.each do |e|
            warn "#{red}#{e}#{clear}"
          end
          total_errors.concat(page_errors)
        end
      end

      unless total_errors.empty?
        raise "#{red}There were YAML errors.#{clear}"
      end
    end
  end
end

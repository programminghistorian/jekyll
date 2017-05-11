module MyModule

  class WarningGenerator < Jekyll::Generator
    def generate(site)

      total_errors = Array.new

      red = "\e[31m"
      clear = "\e[0m"

      lessons = site.pages.keep_if{|i| i.data["layout"] == "default"}

      lessons.each do |p|

        page_errors = Array.new

        if p.data['editors'].nil?
          page_errors.push("'editors' is missing.")
        end

        if p.data["reviewers"].nil?
          page_errors.push("'reviewers' is missing.")
        end

        unit_errors = page_errors.map{|e| "\t - #{e}"}.join("\n")

        unless page_errors.empty?
          warn "#{red}In #{p.dir}#{p.name}:\n#{unit_errors}#{clear}"
          total_errors.concat(page_errors)
        end
      end

      unless total_errors.empty?
        raise "#{red}There were YAML errors.#{clear}"
      end
    end
  end
end

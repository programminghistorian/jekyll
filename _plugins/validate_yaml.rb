module MyModule

  class WarningGenerator < Jekyll::Generator
    def generate(site)

      errors = Array.new

      site.pages.each do |p|
        if p.data['editors'].nil?
           errors.push("On #{p.name}: editors is missing")
        end
      end

      errors.each do |error|
        warn error
      end

      unless errors.empty?
        raise "There were YAML errors."
      end
    end
  end
end

# Plugin to validate the YAML headers of lesson pages.
# Inspired by a very useful answer from Christian: http://stackoverflow.com/a/43909411/3547541

module MyModule

  class WarningGenerator < Jekyll::Generator
    def generate(site)

      # To skip running this plugin, pass skip_yaml_check: true in a config file
      unless site.config["skip_yaml_check"]

      def format_red(error)
        # ANSI codes to color the warnings red
        red = "\e[31m"
        clear = "\e[0m"
        "#{red}#{error}#{clear}"
      end

      # Empty array to collect all errors across the site
      total_errors = Array.new

      # All pages validator

      all_pages = site.pages.select{|i| !i.data["skip_validation"]}

      all_pages.each do |p|

        page_errors = Array.new

          # Warn if any page content contains absolute links
        if Regexp.new("[\\(<]https?://programminghistorian.org/*") =~ p["content"]
          page_errors.push('It looks this page contains a full link to "https://programminghistorian.org". All internal links should start with "/" followed by the relative page path, and not use the full domain name.')
        end

        # Warn if any page content contains inesure image content
        if Regexp.new("\\(http://\\S*(png|svg|jpg|jpeg|gif|tiff)") =~ p["content"]
          page_errors.push('It looks like you are linking to an image using an "http" URL. Make sure all image links use "https".')
        end

        unless page_errors.empty?
          # Throw a warning with the filename
          warn format_red("* In #{p.dir}#{p.name}:")

          # Add some formatting to the errors and then throw them
          unit_errors = page_errors.map{|e| "  - [ ] #{e}"}

          unit_errors.each do |e|
            warn format_red(e)
          end

          # Finally, add all errors on the page to the master error list
          total_errors.concat(page_errors)
        end
      end

      # Lesson validator

      # Collect all valid topics
      valid_topics = site.data["topics"].map{|t| t["type"]}

      # Collect all valid activities
      valid_activites = site.data["activities"].map{|t| t["type"]}

      valid_difficulties = [1, 2, 3]

      # Fields required on ALL lessons
      required_fields = ["layout", "reviewers", "authors", "date", "title", "difficulty", "activity", "topics", "abstract", "editors", "review-ticket", "avatar_alt", "doi"]

      # Fields required only on translated lessons
      trans_required_fields = ["translator", "translation-reviewer", "original", "translation_date", "translation-editor"]

      # Fields required only on original lessons
      original_required_fields = []

      # Find all the pages that represent non-retired lessons
      lessons = site.pages.select{|i| i.data["lesson"] && !i.data["retired"]}

      trans_lessons = site.pages.select{|i| i.data["lesson"] && !i.data["original"]}

      # Collect valid author names from ph_authors.yml
      valid_authors = site.data["ph_authors"].map{|t| t["name"]}

      lessons.each do |p|

        lesson_errors = Array.new
        page_lang = p.data["lang"]

        # Any fields listed in exclude_from_check YAML variable will not be checked.
        excluded_fields = p.data["exclude_from_check"]

        unless excluded_fields.nil? || excluded_fields.empty?
          lesson_required_fields = required_fields - excluded_fields
          trans_lesson_required_fields = trans_required_fields - excluded_fields
          orig_lesson_required_fields = original_required_fields - excluded_fields
        else
          lesson_required_fields = required_fields
          trans_lesson_required_fields = trans_required_fields
          orig_lesson_required_fields = original_required_fields
        end

        # For each required field, check if it is missing on the page. If so, log an error.
        lesson_required_fields.each do |f|
          if p.data[f].nil?
            lesson_errors.push("'#{f}' is missing.")
          end
        end

        # For each activity, topic, or difficulty, check that it is within allowed ranges
        lesson_activity = p.data["activity"]

        unless lesson_activity.nil?
          if !valid_activites.include?(lesson_activity)
              lesson_errors.push("'#{lesson_activity}' is not a valid lesson activity.")
          end
        end

        lesson_topics = p.data["topics"]

        unless lesson_topics.nil?
          if lesson_topics.respond_to?(:each)
            lesson_topics.each do |t|
              if !valid_topics.include?(t)
                lesson_errors.push("'#{t}' is not a valid lesson topic.")
              end
            end
          else
            lesson_errors.push("The lesson topics have not been supplied as a list. Please use either [ ] or - list notation in the lesson YAML.")
          end
        end

        lesson_difficulty = p.data["difficulty"]

        unless lesson_difficulty.nil?
          if !valid_difficulties.include?(lesson_difficulty)
            lesson_errors.push("'#{lesson_difficulty}' is not a valid lesson difficulty.'")
          end
        end

        # Validate date format
        if p.data["date"]
          unless p.data["date"].is_a? Date
            lesson_errors.push("`date` must follow the format YYYY-MM-DD")
          end
        end

        # Check translation required fields
        if p.data["original"]
          trans_lesson_required_fields.each do |f|
            if p.data[f].nil?
              lesson_errors.push("'#{f}' is missing.")
            end
          end

          # Check that the original slug is well-formed
          if Regexp.new("\/") =~ p.data["original"]
            lesson_errors.push('`original` should only contain the original lesson slug, with no other url elements like /en or /lesson')
          end

          if p.data["translation_date"] && p.data["date"]
            if p.data["translation_date"].is_a? Date
              if p.data["date"].is_a? Date
                # Check that translation date is later than publication date
                unless p.data["translation_date"] > p.data["date"]
                  lesson_errors.push("`translation_date` is earlier than original publication `date`.")
                end
              end
            else
              lesson_errors.push("`translation_date` must follow the format YYYY-MM-DD")
          end


          end
        end

        # Check original lesson required fields
        if p.data["original"].nil?
          orig_lesson_required_fields.each do |f|
            if p.data[f].nil?
              lesson_errors.push("'#{f}' is missing.")
            end
          end
        end

        p.data["authors"].each do |a|
          # Check if page author names have exact matches in the ph_authors.yml
          unless valid_authors.include?(a)
            lesson_errors.push("'#{a}' is not currently listed in ph_authors.yml. Check your spelling.")
          end

          # Check that each author has a bio in the page language
          author_entry =  site.data["ph_authors"].select {|e| e["name"] == a }.first
          attempted_bio = author_entry["bio"][page_lang]
          if attempted_bio.nil? || attempted_bio == ""
            lesson_errors.push("'#{a}' does not have a '#{page_lang}' bio in ph_authors.yml.")
          end
        end

        # Check for download links to github
        if Regexp.new("[\\(<]https?://github.com/programminghistorian/.+/blob") =~ p["content"]
          lesson_errors.push('It looks this page contains a full link to data in one of our GitHub repositories. Do not link to GitHub for data. Instead, please use a relative path starting with "/".')
        end

        unless lesson_errors.empty?
          # Throw a warning with the filename
          warn format_red("* In #{p.dir}#{p.name}:")

          # Add some formatting to the errors and then throw them
          unit_errors = lesson_errors.map{|e| "  - [ ] #{e}"}

          unit_errors.each do |e|
            warn format_red(e)
          end

          # Finally, add all errors on the page to the master error list
          total_errors.concat(lesson_errors)
        end
      end

      blog_posts = site.posts

      blog_posts.docs.each do |p|

        post_errors = Array.new

        if p.data["authors"].nil?
          post_errors.push("'authors' field is missing.")
        else
          p.data["authors"].each do |a|
            unless valid_authors.include?(a)
              post_errors.push("'#{a}' is not currently listed in ph_authors.yml. Check your spelling.")
            end
          end
        end

        unless post_errors.empty?
          # Throw a warning with the filename
          warn format_red("* In #{p.data["slug"]}:")

          # Add some formatting to the errors and then throw them
          unit_errors = post_errors.map{|e| "  - [ ] #{e}"}

          unit_errors.each do |e|
            warn format_red(e)
          end

          # Finally, add all errors on the page to the master error list
          total_errors.concat(post_errors)
        end
      end

      # Iff there were page errors, raise an exception that will halt the build
      unless total_errors.empty?
        raise format_red("There were YAML errors.")
      end
    end
  end
end
end

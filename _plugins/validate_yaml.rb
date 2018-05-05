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

      # Collect all valid topics
      valid_topics = site.data["topics"].map{|t| t["type"]}

      # Collect all valid activities
      valid_activites = site.data["activities"].map{|t| t["type"]}

      valid_difficulties = [1, 2, 3]

      # Fields required on ALL lessons
      required_fields = ["layout", "reviewers", "authors", "date", "title", "difficulty", "activity", "topics", "abstract", "editors"] 

      # Fields required only on es lessons
      es_required_fields = ["translator", "translation-reviewer", "original", "translation_date", "translation-editor"]

      # Fields required only on en lessons
      en_required_fields = []

      # Find all the pages that represent non-retired lessons
      lessons = site.pages.select{|i| i.data["lesson"] && !i.data["retired"]}

      # Collect valid author names from ph_authors.yml
      valid_authors = site.data["ph_authors"].map{|t| t["name"]}

      lessons.each do |p|

        page_errors = Array.new

        # Any fields listed in exclude_from_check YAML variable will not be checked.
        excluded_fields = p.data["exclude_from_check"]

        unless excluded_fields.nil? || excluded_fields.empty?
          lesson_required_fields = required_fields - excluded_fields
          es_lesson_required_fields = es_required_fields - excluded_fields
          en_lesson_required_fields = en_required_fields - excluded_fields
        else
          lesson_required_fields = required_fields
          es_lesson_required_fields = es_required_fields
          en_lesson_required_fields = en_required_fields
        end

        # For each required field, check if it is missing on the page. If so, log an error.
        lesson_required_fields.each do |f|
          if p.data[f].nil?
            page_errors.push("'#{f}' is missing.")
          end
        end

        # For each activity, topic, or difficulty, check that it is within allowed ranges
        lesson_activity = p.data["activity"]

        unless lesson_activity.nil?
          if !valid_activites.include?(lesson_activity)
              page_errors.push("'#{lesson_activity}' is not a valid lesson activity.")
          end
        end

        lesson_topics = p.data["topics"]

        unless lesson_topics.nil?
          lesson_topics.each do |t|
            if !valid_topics.include?(t)
              page_errors.push("'#{t}' is not a valid lesson topic.")
            end
          end
        end

        lesson_difficulty = p.data["difficulty"]

        unless lesson_difficulty.nil?
          if !valid_difficulties.include?(lesson_difficulty)
            page_errors.push("'#{lesson_difficulty}' is not a valid lesson difficulty.'")
          end
        end

        # Check Spanish required fields
        if p.data["translated-lesson"]
          es_lesson_required_fields.each do |f|
            if p.data[f].nil?
              page_errors.push("'#{f}' is missing.")
            end
          end
        end

        # Check English required fields
        if p.data["translated-lesson"].nil?
          en_lesson_required_fields.each do |f|
            if p.data[f].nil?
              page_errors.push("'#{f}' is missing.")
            end
          end
        end

        # Check if page author names have exact matches in the ph_authors.yml
        p.data["authors"].each do |a|
          unless valid_authors.include?(a)
            page_errors.push("'#{a}' is not currently listed in ph_authors.yml. Check your spelling.")
          end
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

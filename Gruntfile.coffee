module.exports = (grunt) ->

	grunt.initConfig

		paths:
			src: "src"
			dest: "."

		pkg: grunt.file.readJSON("package.json")

		watch:
			livereload:
				files: [
					"<%= paths.dest %>/assets/**/*.css"
					# "<%= paths.templates %>/**/*"
				]
				options:
					livereload: 7331
			js:
				files: ["<%= paths.src %>/scripts/{,**}/*.coffee"]
				tasks: ["coffee"]
			sass:
				files: ["<%= paths.src %>/styles/{,**}/*.{sass,scss}"]
				tasks: ["compass"]

		connect:
			server:
				options:
					open: true
					livereload: 7331
					port: 1337
					base: '<%= paths.dist %>'


		coffee:
			compile:
				options:
					join: true
				files: [
					"<%= paths.dest %>/assets/build/main.js": [
						"<%= paths.src %>/scripts/*.coffee"
					]
				]


		compass:
			dist:
				options:
					noLineComments: false
					# debugInfo: true
					# bundleExec: true
					sassDir: '<%= paths.src %>/styles'
					cssDir: '<%= paths.dest %>/assets/build'
					environment: 'development'
					require: [

					]

		# copy:
		# 	dist:
		# 		files: [

		# 		]

		# shell:
		# 	flask:
		# 		command: 'cd flask; python server.py'
		# 		options:
		# 			stdout: true
		# 			stderr: true
		# 			stdin: true
		# 			async: true

		# concurrent:
		# 	dev:
		# 		tasks: ['shell:flask', 'watch']
		# 		options:
		# 			logConcurrentOutput: true


	grunt.loadNpmTasks("grunt-contrib-coffee")
	grunt.loadNpmTasks("grunt-contrib-connect")
	grunt.loadNpmTasks("grunt-contrib-watch")
	grunt.loadNpmTasks("grunt-contrib-compass")
	grunt.loadNpmTasks("grunt-shell")
	grunt.loadNpmTasks("grunt-concurrent")
	grunt.loadNpmTasks("grunt-notify")

	# grunt.registerTask "server", ['shell:flask']

	grunt.registerTask "default", [
		'coffee'
		'compass'
		'connect'
		'watch'
	]

# npm install --save-dev \
# grunt \
# grunt-contrib-coffee \
# grunt-contrib-connect \
# grunt-contrib-watch \
# grunt-contrib-compass \
# grunt-contrib-copy \
# grunt-notify
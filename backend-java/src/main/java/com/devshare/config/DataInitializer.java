package com.devshare.config;

import com.devshare.entity.User;
import com.devshare.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class DataInitializer implements CommandLineRunner {
    private final UserRepository userRepository;

    @Autowired
    public DataInitializer(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public void run(String... args) {
        if (userRepository.count() == 0) {
            User admin = new User();
            admin.setName("DevShare");
            admin.setEmail("admin@devshare.com");
            admin.setBio("热爱编程，乐于分享。这个平台展示了如何使用多种编程语言构建一个现代化的全栈应用。");
            admin.setGithub("https://github.com/devshare");
            admin.setAvatar("D");
            userRepository.save(admin);
        }
    }
}